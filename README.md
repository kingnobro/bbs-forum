# bbs-forum
基于 Flask 的个人论坛



部署地址：[点我](http://150.158.166.153/) (之前购买的域名过期了，所以目前直接使用 ip 地址)

测试账号：test

测试密码：123



### 简介

- 使用 **Nginx** 反向代理静态资源，提升访问性能
- 利用 **Gevent** 替换多线程为协程，减少上下文切换开销
- **Gunicorn** 托管多 worker，发挥多核优势，实现单机负载均衡，并使用 **Supervisor** 进行管理
- 利用 **Redis** 加速热点路由，减少重复的数据库多表查询次数
- 利用加盐，加强密码安全
- 利用 **token** 防御 CSRF 攻击
- 基于 **Celery** 的消息队列处理邮件发送
- 话题编辑支持 Markdown 实时渲染
- 图片**异步上传**并回调自动填写
- 编写 **Shell** 脚本，实现在服务器上一键部署



### 部署环境

- Ubuntu
- Python3.6



### 主要功能

- 用户模块：注册、登录、头像签名修改、密码找回
- 论坛模块：发布评论、标签检索、帖子时间排序
- 私信模块：用户发送私信、站内@、邮件通知



### 功能演示

##### 用户注册

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vj8idqgg30jg09utwx.gif)

- 注册时需要填写用户名、密码和邮箱
- 邮箱可用于密码找回、站内信通知



##### 用户登录

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vix8jt3g30lk0b4wnj.gif)

- 填写正确的用户账号和密码即可登录论坛
- 测试账号：test    测试密码：123



##### 发帖

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vjukycag31380fmtsj.gif)

- 可在论坛内发送主题帖
- 内容支持 Markdown 渲染



##### 回帖

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vk98f4yg31380fm1kx.gif)

- 在主题帖下可发表回复



##### 更改头像

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vkog8tjg30jg09uqdk.gif)

<img src="https://tva1.sinaimg.cn/large/008eGmZEgy1go0vl5u9gmj30h4098dft.jpg" style="zoom:50%;" />

- 支持 gif、jpg、jpeg 格式的头像



##### 更改个性签名

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vlo72rng310y09u48k.gif)



##### 站内私信

发送：

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vlz13k7g30gm09u4db.gif)

- 给指定用户发送站内私信
- 发送后会邮件通知对应用户



查看：

![](https://tva1.sinaimg.cn/large/008eGmZEgy1go0vmajgcig312a0eqah4.gif)