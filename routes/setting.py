from flask import (
    render_template,
    request,
    Blueprint,
    redirect,
    url_for,
    abort
)
from werkzeug.datastructures import FileStorage

from routes import current_user
from models.user import User
from utils import log
import uuid
import os

main = Blueprint('setting', __name__)


@main.route('/')
def index():
    u = current_user()
    return render_template('setting.html', user=u)


@main.route('/name', methods=['POST'])
def setting_name():
    u = current_user()
    form = request.form

    signature = form['signature']
    username = form['username']
    if len(signature) == 0:
        signature = u.signature

    User.update(u.id, signature=signature, username=username)
    return redirect(url_for('.index'))


@main.route('/password', methods=['POST'])
def setting_password():
    u = current_user()
    form = request.form
    old_pass = User.salted_password(form['old_pass'])
    new_pass = User.salted_password(form['new_pass'])

    if old_pass == u.password:
        User.update(u.id, password=new_pass)

    return redirect(url_for('setting.index'))


@main.route('/image/add', methods=['POST'])
def avatar_add():
    file: FileStorage = request.files['avatar']
    suffix = file.filename.split('.')[-1]
    if suffix not in ['gif', 'jpg', 'jpeg']:
        abort(400)
        log('不接受的后缀, {}'.format(suffix))
    else:
        filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
        path = os.path.join('images', filename)
        file.save(path)

        u = current_user()
        User.update(u.id, image='/images/{}'.format(filename))

        return redirect(url_for('.index'))
