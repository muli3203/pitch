from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,ValidationError,SubmitField
from wtforms.validators import Required
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password  = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    password_confirm =PasswordField('Confrim Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email already exists")

    def validate_username(self,data_field):
        if User.query.filter_by(username= data_field.data).first():
            raise ValidationError("Username already exists")