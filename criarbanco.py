from config import app, db
from models import User, Event

with app.app_context():
    db.create_all()
    