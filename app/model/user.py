from app import db
from datetime import datetime

class User(db.Model):
    # membuat stuktur database
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # merepresentasikan Class User
    def __repr__(self):
        return '<User {}>'.format(serlf.name)
