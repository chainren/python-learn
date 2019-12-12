from flask import Flask, render_template, redirect

from myForm import MyForm, ProfileForm, PhotoForm

from werkzeug import secure_filename

import os

app = Flask(__name__)

# 定义secret_key，用于csrf
app.secret_key = 'abc'

# app配置
app.config['UPLOAD_FOLDER'] = './upload'


@app.route('/', methods=['GET', 'POST'])
def myform_submit():
    # 实例化form
    form = MyForm()
    # 验证表单
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('myform.html', form=form)


@app.route('/success')
def success():
    return "success"


# 上传文件表单
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    filepath = None
    if form.validate_on_submit():
        # 使用secure_filename
        filename = secure_filename(form.photo.data.filename)
        file = form.photo.data
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    else:
        filename = None
    return render_template('photo.html', form=form, filename=filename)


if __name__ == '__main__':
    app.run(port=8888, debug=True)
