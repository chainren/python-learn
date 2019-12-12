from flask import Flask

import myfilter

# Flask提供的 render_template函数把Jinja2模板引擎集成到了程序中
from flask import render_template

# 创建应用
app = Flask('template-demo')

# 注册过滤器
env = app.jinja_env
env.filters['mylen'] = myfilter.mylen
env.filters['omit'] = myfilter.omit


@app.route("/")
def index():
    return "Welcome!"

# 定义路由
@app.route("/sayhello/<name>")
def sayhello(name):
    # 渲染视图，并将视图参数传入
    return render_template("hello.html", name=name)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
