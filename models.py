"""Models for Blogly."""
import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 

    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    image_url = db.Column(db.String)
    
    def __repr__(self):
        u=self
        return f"<User first_name= {u.first_name}  last_name= {u.last_name}  url= {u.image_url}"


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 

    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    users = db.relationship('User', backref='posts')

    def __repr__(self):
        p=self
        return f"<Post id= {p.id}  title= {p.title}  content= {p.content} user_id= {p.user_id}"