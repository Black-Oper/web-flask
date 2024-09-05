from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length

# Classe base para formulario de cadastro de uma pessoa(nome, senha)
class FormCadastrar(FlaskForm):
    # Define a variavel 'nome' e 'senha' como tipo 'String' e usa validators que sao parametros para validacao do cadastro
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=45)]) 
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
    

class FormLogar(FlaskForm):
    # Verifica se o nome e a senha foram validados corretamente
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class FormEvent(FlaskForm):
    
    event_name = StringField('Nome do evento', validators=[DataRequired()])
    event_date = DateField('Data do evento', validators=[DataRequired()])
    event_description = TextAreaField('Descrição do evento', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Evento')
