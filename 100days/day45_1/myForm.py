# 定义form

from flask_wtf import FlaskForm

from wtforms import StringField, DateField, RadioField, SelectMultipleField, SubmitField

from wtforms.validators import DataRequired, InputRequired, Length


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


# 定义一个个人信息表单
class InfoForm(FlaskForm):
    name = StringField(label="姓名", validators=[InputRequired()])
    city = StringField(u"城市")
    birthday = DateField(label="生日", format="%Y-%m-%d")
    gender = RadioField(label="性别", choices=[(1, 'male'), (0, 'female')])
    interest = SelectMultipleField(
        label="兴趣", choices=[(1, 'Football'), (2, 'Movies'), (3, 'Reading')])
