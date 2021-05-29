from .. import db
from app import login
from flask_login import UserMixin

class User(UserMixin,db.Document):
    user_id = db.SequenceField()
    full_name = db.StringField()
    username = db.StringField()

@login.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()