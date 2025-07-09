from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,PasswordField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    cpf = IntegerField('cpf', validators=[DataRequired()])
    senha = PasswordField['password', PasswordField]