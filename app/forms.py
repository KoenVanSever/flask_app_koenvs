from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField  # BooleanField
from wtforms.validators import Required, Email, EqualTo
import email_validator


class LoginForm(FlaskForm):
    email = TextField('Email Address', [Email(),
                                        Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        Required(message='Must provide a password. ;-)')])


class RegisterForm(FlaskForm):
    username = TextField("Username", [Required()])
    email = TextField('Email Address', [Email(), Required()])
    password = PasswordField('Password', [Required()])
    repeat_password = PasswordField('Repeat password', [Required()])
    role = TextField('Role')
    status = TextField('Status')
