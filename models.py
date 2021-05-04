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
    posttag = db.relationship('PostTag', backref='posts')
    tags = db.relationship('Tag', secondary='posts_tags', backref='posts')

    def __repr__(self):
        p=self
        return f"<Post id= {p.id}  title= {p.title}  content= {p.content} user_id= {p.user_id}"

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    name = db.Column(db.String, nullable = False, unique=True)
    
    posttag = db.relationship('PostTag', backref='tags')

    def __repr__(self):
        t=self
        return f"<Tag id= {t.id}  name= {t.name}>"


class PostTag(db.Model):
    """Mapping of a post to a tag"""
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key = True) 
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)
    
    