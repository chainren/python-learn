from flask import Flask, render_template

from flask_bootstrap import Bootstrap


app = Flask("flask-bootstrap")

# 为应用初始化bootstrap 给应用加载 bootstrap 主要是给应用加上 Jinja2 的扩展
bootstrap = Bootstrap(app)
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True # 设置为使用本地资源


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/mybooks')
def mybooks():
    mybooks = ["《redis原理与实践》","《深入理解java虚拟机》","《项目管理知识体系指南》"]
    return render_template('book_list.html', mybooks=mybooks)

if __name__ == '__main__':
    app.run(port=8888, debug=True)
