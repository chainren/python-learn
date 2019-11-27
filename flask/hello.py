# -*- coding:utf-8 -*-

"""
author chenrg
flask 示例
"""


from flask import Flask
from flask import request, g, Response, make_response, render_template


# 创建一个应用
app = Flask(__name__)

# 定义接口路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 动态路由
@app.route('/sayhello/<name>', methods=['GET'])
def sayHello(name):
    return '<h1>Hello %s</h1>' % name


# 模拟提交表单
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError as e:
        return 'form incorrect'
    if username == 'admin' and password == 'admin':
        return 'login success'
    else:
        return 'login error'


# 勾子方法，用于在请求之前拦截请求，做一些前置操作。比如权限检查等
@app.before_request
def before_request():
    print('Before request method: %s' % request.method)


# @app.errorhandler 修饰符，会将一个响应代码映射到一个视图函数上，这里是将404(找不到页面)码，处理成一个个性的错误页面
# 使用make_response构建响应
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['User-agent'] = 'Firefox'
    return resp

# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
