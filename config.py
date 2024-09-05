from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# inicia o app
app = Flask(__name__)

# configurações do app
app.config['SECRET_KEY'] = 'quartetoprogramastico'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_manager.db'

# inicializa o banco de dados
db = SQLAlchemy()
db.init_app(app)

# inicializa o login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
