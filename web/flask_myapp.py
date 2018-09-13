# -*- coding:utf-8 -*-


# 使用flask框架编写一个web程序
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来

from flask import Flask
from flask import request

app = Flask(__name__)


# 定义首页
@app.route('/', methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 从request对象中获取表单内容
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()