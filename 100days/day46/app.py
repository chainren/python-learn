
from flask import Flask

from flask_sql
from flask import Flask, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField
from wtforms.validators import DataRequired, InputRequired
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'abc'
# 定义数据库连接 格式:mysql://<用户名>:<密码>@:<端口>/数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://develop:xs_dev@10.200.3.2:3306/test'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
# 实例化db
db = SQLAlchemy(app)


# 定义数据模型
class Profile(db.Model):

    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))
    birthday = db.Column(db.Date())
    createtime = db.Column(db.DateTime())
    about = db.Column(db.Text())


class ProfileForm(FlaskForm):
    name = StringField(label='姓名', validators=[InputRequired()])
    birthday = DateField(label='生日', format="%Y-%m-%d",
                         validators=[DataRequired('日期格式不正确')])
    about = StringField(label="简介", validators=[InputRequired()])

@app.route('/myprofile/<int:id>/')
def myprofile(id):
     # 利用参数 id 读取数据库记录
    profile = Profile.query.get(id)
    # 将结果送给模板做展示
    return render_template('profile.html', profile=profile)


@app.route('/createprofile', methods=('GET', 'POST'))
def createprofile():
    form = ProfileForm()
    if form.validate_on_submit():  # 如果表单提交了 用表单数据创建 Profile 对象
        profile = Profile()
        profile.name = form.name.data
        profile.birthday = form.birthday.data
        profile.about = form.about.data or ""
        profile.createtime = datetime.now()
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('myprofile', id=profile.id))  # 跳转到展示页面
    else:
        return render_template('createprofile.html', form=form)  # 显示创建页面


if __name__ == '__main__':

    # 删除表
    # db.drop_all()
    # 创建数据表
    # db.create_all()

    app.run(port=8888, debug=True)