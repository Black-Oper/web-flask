from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
from models import StatusEnum

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
    event_status = SelectField('Status', choices=[
        (StatusEnum.NOT_STARTED.name, StatusEnum.NOT_STARTED.value),
        (StatusEnum.IN_PROGRESS.name, StatusEnum.IN_PROGRESS.value),
        (StatusEnum.FINISHED.name, StatusEnum.FINISHED.value)
    ], validators=[DataRequired()], default=StatusEnum.NOT_STARTED.name)
    submit = SubmitField('Cadastrar Evento')
