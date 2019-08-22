from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length, InputRequired


class LoginForm(FlaskForm):
    username = StringField(
        label="Usuário",
        validators=[
            InputRequired(message="Por favor informe seu nome de usuário"),
            Length(min=3, message="Usuário não pode ser menor que 3 caracteres"),
            Length(max=10, message="Usuário não pode ser maior que 10 caracteres")
        ]
    )
    password = PasswordField(
        label="Senha",
        validators=[
            InputRequired(message="Por favor informe sua senha"),
            Length(min=5, message="Senha não pode ser menor que 5 caracteres"),
            Length(max=10, message="Senha não pode ser maior que 15 caracteres")
        ]
    )


class RegisterForm(FlaskForm):
    username = StringField(
        label="Usuário",
        validators=[
            InputRequired(message="Por favor informe seu nome de usuário"),
            Length(min=3, message="Usuário não pode ser menor que 3 caracteres"),
            Length(max=10, message="Usuário não pode ser maior que 10 caracteres")
        ]
    )
    full_name = StringField(
        label="Nome Completo",
        validators=[
            InputRequired(message="Por favor informe seu nome completo"),
            Length(min=5, message="Nome Completo não pode ser menor que 5 caracteres"),
            Length(max=120, message="Nome Completo não pode ser maior que 120 caracteres")
        ]
    )
    password = PasswordField(
        label="Senha",
        validators=[
            InputRequired(message="Por favor informe sua senha"),
            Length(min=5, message="Senha não pode ser menor que 5 caracteres"),
            Length(max=10, message="Senha não pode ser maior que 15 caracteres")
        ]
    )


class RegisterAreasForm(FlaskForm):
    cultura = IntegerField(
        label="Cultura",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="cultura.png"
    )
    economia = IntegerField(
        label="Economia",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="economia.png",
    )
    educacao = IntegerField(
        label="Educação",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="educacao.png"
    )
    meio_ambiente = IntegerField(
        label="Meio Ambiente",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="meio_ambiente.png"
    )
    saude = IntegerField(
        label="Saúde",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="saude.png"
    )
    seguranca = IntegerField(
        label="Segurança",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="seguranca.png"
    )
    tecnologia = IntegerField(
        label="Tecnologia",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="tecnologia.png"
    )
    '''
    cultura = IntegerField(label="Cultura", validators=[DataRequired(), NumberRange(min=1, max=5)])
    economia = IntegerField(label="Economia", validators=[DataRequired(), NumberRange(min=1, max=5)])
    educacao = IntegerField(label="Educação", validators=[DataRequired(), NumberRange(min=1, max=5)])
    meio_ambiente = IntegerField(label="Meio Ambiente", validators=[DataRequired(), NumberRange(min=1, max=5)])
    saude = IntegerField(label="Saúde", validators=[DataRequired(), NumberRange(min=1, max=5)])
    seguranca = IntegerField(label="Segurança", validators=[DataRequired(), NumberRange(min=1, max=5)])
    tecnologia = IntegerField(label="Tecnologia", validators=[DataRequired(), NumberRange(min=1, max=5)])
    '''

class RateCandidateForm(FlaskForm):
    candscore = IntegerField(
        label="Candidato",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ]
    )

class RateCandidatesForm(FlaskForm):
    alckmin = IntegerField(
        label="Geraldo Alckmin",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="alckmin.png"
    )
    amoedo = IntegerField(
        label="João Amoêdo",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="amoedo.png"
    )
    bolsonaro = IntegerField(
        label="Jair Bolsonaro",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="bolsonaro.png"
    )
    ciro = IntegerField(
        label="Ciro Gomes",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="ciro.png"
    )
    daciolo = IntegerField(
        label="Cabo Daciolo",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="daciolo.png"
    )
    boulos = IntegerField(
        label="Guilherme Boulos",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="boulos.png"
    )
    haddad = IntegerField(
        label="Fernando Haddad",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="haddad.png"
    )
    marina = IntegerField(
        label="Marina Silva",
        validators=[
            InputRequired(),
            NumberRange(min=1, max=5)
        ],
        description="marina.png"
    )

    '''
    alckmin = IntegerField(label="Geraldo Alckmin", validators=[DataRequired(), NumberRange(min=1, max=5)])
    amoedo = IntegerField(label="João Amoêdo", validators=[DataRequired(), NumberRange(min=1, max=5)])
    bolsonaro = IntegerField(label="Jair Bolsonaro", validators=[DataRequired(), NumberRange(min=1, max=5)])
    ciro = IntegerField(label="Ciro Gomes", validators=[DataRequired(), NumberRange(min=1, max=5)])
    daciolo = IntegerField(label="Cabo Daciolo", validators=[DataRequired(), NumberRange(min=1, max=5)])
    boulos = IntegerField(label="Guilherme Boulos", validators=[DataRequired(), NumberRange(min=1, max=5)])
    haddad = IntegerField(label="Fernando Haddad", validators=[DataRequired(), NumberRange(min=1, max=5)])
    marina = IntegerField(label="Marina Silva", validators=[DataRequired(), NumberRange(min=1, max=5)])
    '''
