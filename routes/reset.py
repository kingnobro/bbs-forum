from flask import (
    render_template,
    request,
    Blueprint,
    redirect,
    url_for,
)
from models.user import User
from models.message import Messages
import uuid

main = Blueprint('reset', __name__)

id_of_token = dict()


@main.route('/index')
def index():
    return render_template('reset_index.html')


@main.route('/send', methods=['POST'])
def send():
    u: User = User.one(email=request.form['email'])
    token = str(uuid.uuid4())
    id_of_token[token] = u.id
    content = 'http://118.24.247.186/reset/view?token={}'.format(token)

    # 发邮件
    Messages.send(
        title='找回密码',
        content=content,
        sender_id=1,
        receiver_id=u.id,
    )
    return redirect('/')


@main.route('/view')
def view():
    return render_template('view.html')


@main.route('/update', methods=['POST', 'GET'])
def update():
    form = request.form.to_dict()
    token = str(request.referrer).split('=')[-1]
    user_id = id_of_token[token]

    u = User.one(id=user_id)
    new_password = User.salted_password(form['new_pass'])
    User.update(u.id, password=new_password)

    return redirect('/')
