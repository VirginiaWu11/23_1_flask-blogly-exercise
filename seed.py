"""Seed file to make sample data for blogly db."""
from models import User, db
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
