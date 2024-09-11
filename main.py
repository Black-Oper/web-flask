# seção de imports
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from config import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from models import Event, User
from models import StatusEnum

# rota principal do site
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Faz o cadastro do usuario
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    # Faz a validacao através da funcao 'validate_on_submit()'
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        
        user_exists = User.query.filter_by(name=username).first()

        if user_exists:
            return render_template('register.html', form=form, user_exists=user_exists)
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
    form = LoginForm()

    if form.validate_on_submit():
        usernameLogin = form.username.data
        usernameBank = User.query.filter_by(name=usernameLogin).first()
        
        if usernameBank:
            passwordLogin = form.password.data
            passwordBank = usernameBank.password
            
            if check_password_hash(passwordBank, passwordLogin):
                login_user(usernameBank)
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', form=form, invalid_user=True)
        else:
            return render_template('login.html', form=form, invalid_user=True)

    return render_template('login.html', form=form)


# Rota para logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Rota para dashboard
@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    users = User.query.all()
    filter_status = request.args.get('filter')

    if filter_status:
        events = Event.query.filter_by(user_id=current_user.id, status=filter_status).all()
    else:
        events = Event.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard.html', events=events, filter=filter_status)
# Rota para criar um novo evento
@app.route('/new_event', methods=['GET', 'POST'])
@login_required
def new_event():

    from forms import EventForm
    
    form = EventForm()
    
    if form.validate_on_submit():
        
        name = form.event_name.data
        date = form.event_date.data
        description = form.event_description.data
        status = form.event_status.data
        
        new_event = Event(name=name, date=date, description=description, status=status, user_id=current_user.id)
        
        db.session.add(new_event)
        db.session.commit()
        
        return redirect(url_for('dashboard'))
    
    return render_template('new_event.html', form=form)

@app.route('/event_assignment', methods=['GET', 'POST'])
@login_required
def event_assignment():
    from forms import EventForm
    _id = request.args.get('id')
    print(f"User ID from request: {_id}")

    form = EventForm()

    if form.validate_on_submit():
        name = form.event_name.data
        date = form.event_date.data
        description = form.event_description.data
        status = form.event_status.data

        new_event = Event(name=name, date=date, description=description, status=status, user_id=_id)
        print(f"New Event User ID: {new_event.user_id}")

        db.session.add(new_event)
        db.session.commit()

        flash(f'Tarefa "{name}" atribuída com sucesso!', 'success')
        return redirect(url_for('atribuir_tarefa'))

    return render_template('new_event.html', form=form, user_id=_id)


# Rota para editar um evento
@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    from forms import EventForm
    
    event = Event.query.get(event_id)
    
    form = EventForm()
    
    if form.validate_on_submit():
        event.name = form.event_name.data
        event.date = form.event_date.data
        event.description = form.event_description.data
        event.status = form.event_status.data

        db.session.commit()

        return redirect(url_for('dashboard'))

    # Preenche o formulário com os dados existentes do evento
    form.event_name.data = event.name
    form.event_date.data = event.date
    form.event_description.data = event.description

    return render_template('edit_event.html', form=form)


# Rota para deletar um evento
@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    
    event = Event.query.get_or_404(event_id)

    db.session.delete(event)
    db.session.commit()

    return redirect(url_for('dashboard'))

@app.route('/atribuir_tarefa', methods=['GET', 'POST'])
@login_required
def atribuir_tarefa():
    users = User.query.all()
    event = Event.query.all()
    
    return render_template('tasksatt.html', users=users, event=event)

# Executar o Flask
if __name__ == "__main__":
    app.run(debug=True)
