from flask_login import UserMixin
from config import db, login_manager
from sqlalchemy import Enum
import enum

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    events = db.relationship('Event', backref='user', lazy=True)
    

class StatusEnum(enum.Enum):
    NOT_STARTED = 'Não Iniciada'
    IN_PROGRESS = 'Em Progresso'
    FINISHED = 'Concluída'
    
    
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(Enum(StatusEnum), nullable=False, default=StatusEnum.NOT_STARTED.name)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    