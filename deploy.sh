#!/usr/bin/env bash
# 1. 拉代码到 /var/www/web19
# 2. 执行 bash deploy.sh

set -ex

# 系统设置
apt-get install -y curl ufw
ufw allow 22
ufw allow 80
ufw allow 443
ufw allow 465
ufw default deny incoming
ufw default allow outgoing
ufw status verbose
ufw -f enable

# redis 需要 ipv6
sysctl -w net.ipv6.conf.all.disable_ipv6=0
# 安装过程中选择默认选项，这样不会弹出 libssl 确认框
export DEBIAN_FRONTEND=noninteractive
# 装依赖
apt-get install -y git supervisor nginx python3-pip mysql-server redis-server apache2-utils
#apt-get install -y git supervisor nginx python3-pip mysql-server apache2-utils
pip3 install jinja2 flask gevent gunicorn pymysql flask_sqlalchemy flask_mail marrow.mailer redis Celery
#pip3 install jinja2 flask gevent gunicorn pymysql flask_sqlalchemy flask_mail marrow.mailer

# 删掉 nginx default 设置
rm -f /etc/nginx/sites-enabled/default
rm -f /etc/nginx/sites-available/default
# 不要再 sites-available 里面放任何东西
cp /var/www/web19/web19.nginx /etc/nginx/sites-enabled/web19
chmod -R o+rwx /var/www/web19

cp web19.service /etc/systemd/system/web19.service
cp web19-message-queue.service /etc/systemd/system/web19-message-queue.service


# 初始化
cd /var/www/web19
python3 reset.py

# 重启服务器
systemctl daemon-reload
systemctl restart web19
systemctl restart web19-message-queue
systemctl restart nginx

echo 'succsss'
echo 'ip'
hostname -I
curl http://localhost
