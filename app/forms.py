from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import Required, Length
from wtforms.validators import EqualTo
from .models import User


# 登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(1, 20)])
    account = StringField('账号', validators=[Required(), Length(1, 20)])
    password = PasswordField('密码', validators=[Required(), Length(1, 20)])
    sumit = SubmitField('登录')


# 注册表单
class RegisterFrom(FlaskForm):
    username = StringField('用户', validators=[Required(), Length(1, 20)])
    account = StringField('账号', validators=[Required(), Length(1, 20)])
    password = PasswordField('密码', validators=[Required(), Length(
        1, 20), EqualTo('password2', message='密码必须匹配')])
    password2 = PasswordField('确认密码', validators=[Required(), Length(1, 20)], )
    sumit = SubmitField('注册')

    # def validate_username(self, field):
      #  user = User(username=field.data)
       # return True

    # def validate_account(self, field):
     #   user = User(username=field.data)
      #  return True
    
