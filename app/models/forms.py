from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField(label="Usuário", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired()])
