from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length

# Classe base para formulário de cadastro de uma pessoa (CPF, nome, senha)
class RegisterForm(FlaskForm):
    # Define os campos e usa 'validators' para validação
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=45)]) 
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

# Formulário de login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Formulário de evento
class EventForm(FlaskForm):
    event_name = StringField('Nome do evento', validators=[DataRequired()])
    event_date = DateField('Data do evento', validators=[DataRequired()], format='%Y-%m-%d')  # Formato de data ISO
    event_description = TextAreaField('Descrição do evento', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Evento')
