from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    username = StringField(label="Usuário", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField(label="Usuário", validators=[DataRequired()])
    full_name = StringField(label="Nome", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired()])


class RegisterAreasForm(FlaskForm):
    cultura = IntegerField(label="Cultura", validators=[DataRequired(), NumberRange(min=1, max=5)])
    economia = IntegerField(label="Economia", validators=[DataRequired(), NumberRange(min=1, max=5)])
    educacao = IntegerField(label="Educação", validators=[DataRequired(), NumberRange(min=1, max=5)])
    meio_ambiente = IntegerField(label="Meio Ambiente", validators=[DataRequired(), NumberRange(min=1, max=5)])
    saude = IntegerField(label="Saúde", validators=[DataRequired(), NumberRange(min=1, max=5)])
    seguranca = IntegerField(label="Segurança", validators=[DataRequired(), NumberRange(min=1, max=5)])
    tecnologia = IntegerField(label="Tecnologia", validators=[DataRequired(), NumberRange(min=1, max=5)])


class RateCandidatesForm(FlaskForm):
    alckmin = IntegerField(label="Geraldo Alckmin", validators=[DataRequired(), NumberRange(min=1, max=5)])
    amoedo = IntegerField(label="João Amoêdo", validators=[DataRequired(), NumberRange(min=1, max=5)])
    bolsonaro = IntegerField(label="Jair Bolsonaro", validators=[DataRequired(), NumberRange(min=1, max=5)])
    ciro = IntegerField(label="Ciro Gomes", validators=[DataRequired(), NumberRange(min=1, max=5)])
    daciolo = IntegerField(label="Cabo Daciolo", validators=[DataRequired(), NumberRange(min=1, max=5)])
    boulos = IntegerField(label="Guilherme Boulos", validators=[DataRequired(), NumberRange(min=1, max=5)])
    haddad = IntegerField(label="Fernando Haddad", validators=[DataRequired(), NumberRange(min=1, max=5)])
    marina = IntegerField(label="Marina Silva", validators=[DataRequired(), NumberRange(min=1, max=5)])
