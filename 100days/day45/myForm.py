# Flask-WTF 表单使用

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField, SelectMultipleField
from flask_wtf.file import FileField

from wtforms.validators import DataRequired, InputRequired, Length


class MyForm(FlaskForm):
    # 定义表单
    name = StringField('name', validators=[DataRequired()])


class ProfileForm(FlaskForm):
    name = StringField(label='姓名', validators=[InputRequired()])
    city = StringField('城市', validators=[Length(
        min=4, max=25, message='输入的长度不符合要求')])
    birthday = DateField(label='生日', format="%Y-%m-%d",
                         validators=[DataRequired('日期格式不正确')])
    gender = RadioField(label='性别', choices=[(1, 'male'), (2, 'female')])
    interest = SelectMultipleField(
        label='兴趣', choices=[(1, 'Football'), (2, 'Movies'), (3, 'Reading')])


class PhotoForm(FlaskForm):
    photo = FileField(u'上传照片')
