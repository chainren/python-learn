
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from user_store import User, get_user

from forms import LoginForm


app = Flask(__name__)

app.secret_key = 'abc123'

# 实例化登录管理对象
login_manager = LoginManager()
# 初始化应用
login_manager.init_app(app)
# 设置用户登录视图函数
login_manager.login_view = 'login'


# 加载登录用户
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# 定义登录接口
@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)
        if user_info is None:
            emsg = "用户名或密码错误"
        else:
            user = User(user_info)
            # 校验密码
            if user.verify_pwd(password):
                login_user(user)
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码错误"
    return render_template('login.html', form=form, emsg = emsg)

# 需登录才能访问
@app.route('/')
@login_required
def index():
    return render_template('index.html', username = current_user.username)

@app.route('/logout')
@login_required
def logout():
    # 注销当前用户
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
