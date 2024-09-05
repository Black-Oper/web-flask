# seção de imports
from flask import Flask, redirect, render_template, url_for
from flask_login import login_user, logout_user
from config import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm  # Certifique-se de que LoginForm esteja correto
from models import User

# rota principal do site
@app.route("/")
def index():
    return render_template('index.html')


# Faz o cadastro do usuario
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    # Faz a validacao através da funcao 'validate_on_submit()'
    if form.validate_on_submit():
        # cpf = form.cpf.data
        username = form.username.data
        password = generate_password_hash(form.password.data)
        
        user_exists = User.query.filter_by(name=username).first()

        if user_exists:
            # Dê feedback ao usuário sobre o erro
            return render_template('register.html', form=form, message="Usuário já existe!")
        else:
            # Cria novo usuário e salva no banco de dados
            new_user = User(name=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


# Faz o login do usuario
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Certifique-se de que o nome do formulário esteja correto

    if form.validate_on_submit():
        usernameLogin = form.username.data
        usernameBank = User.query.filter_by(username=usernameLogin).first()
        
        if usernameBank:
            passwordLogin = form.password.data
            passwordBank = usernameBank.password
            
            if check_password_hash(passwordBank, passwordLogin):
                login_user(usernameBank)
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', form=form, message="Senha incorreta.")
        else:
            return render_template('login.html', form=form, message="Usuário não encontrado.")

    return render_template('login.html', form=form)

# Rota para logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Executar o Flask
if __name__ == "__main__":
    app.run(debug=True)
