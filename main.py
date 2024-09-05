from flask import Flask, redirect, render_template, url_for
from flask_login import login_user
from config import app, db

from forms import FormCadastrar
from werkzeug.security import generate_password_hash

from models import User

@app.route("/")
def index():
    return 'teste'

# Faz o cadastro do usuario
@app.route("/register", methods=['GET', 'POST']) # url
def cadastrar():
    # Importa do forms o formulario para cadastro de usuario
    form = FormCadastrar()
    # Faz a validacao atravez da funcao 'validate_on_submit()' para verificar se esta nos padroes de formulario
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        
        username_exists = User.query.filter_by(username=username).first()

        if(username_exists):
            print("Usuario ja existe!")
        else:
            # Cria um novo usuario, adiciona no banco de dados e redireciona para a página de login
            new_username = User(username=username, password=password)
            db.session.add(new_username)
            db.session.commit()
            return redirect(url_for('Registro'))

    return render_template('register.html', form=form)

@app.route("/login")
def login():
    return 'teste login'
