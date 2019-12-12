'''
Flask-WTF 表单框架
pip install Flask-WTF
'''

from flask import Flask, redirect, render_template, request

from myForm import MyForm, InfoForm

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 定义密钥， 用于CSRF 校验
app.secret_key = 'abc'


@app.route('/', methods=['GET', 'POST'])
def my_first_form():

    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('myform.html', form=form)


@app.route('/success')
def success():
    return 'success'


@app.route('/info', methods=['GET', 'POST'])
def info_form():
    form = InfoForm()
    if form.is_submitted():
        info = dict()
        info['name'] = request.form.get("name")
        info['city'] = request.form.get("city")
        info['gender'] = request.form.get("gender")
        info['birthday'] = request.form.get("birthday")
        info['interest'] = request.form.get("interest")
        print(info)
        return info
    return render_template('infoForm.html', form=form)


# 启动app
if __name__ == '__main__':
    app.run(port=9999, debug=True)
