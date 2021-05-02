"""Seed file to make sample data for blogly db."""
from models import User, db, Post
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Empty table
User.query.delete()

# Add users
joel = User(first_name= 'Joel', last_name = 'Burton', image_url="https://images.unsplash.com/photo-1530813089459-29f31dd229c2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3F1YXJlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60")
spike = User(first_name= 'Spike', last_name = 'M.', image_url="https://images.unsplash.com/photo-1530813089459-29f31dd229c2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3F1YXJlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60")
whiskey = User(first_name= 'Whiskey', last_name = 'C.', image_url="https://images.unsplash.com/photo-1530813089459-29f31dd229c2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3F1YXJlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60")

# Add new objects to session
db.session.add(joel)
db.session.add(spike)
db.session.add(whiskey)

# Commit
db.session.commit()

# Add posts
p1 = Post(title='hi', content='test1', user_id= 1)
p2 = Post(title='hi2', content='test2', user_id= 1)
p3 = Post(title='hi3', content='test3', user_id= 3)

# Add new objects to session
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

# Commit
db.session.commit()