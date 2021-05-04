"""Seed file to make sample data for blogly db."""
from models import User, db, Post, Tag, PostTag
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
p3 = Post(title='hi3', content='test3', user_id= 2)
p4 = Post(title='hello1', content='test3', user_id= 2)
p5 = Post(title='world1', content='test3', user_id= 2)
p6 = Post(title='hi4', content='test3', user_id= 3)
p7 = Post(title='hi7', content='test3', user_id= 3)
p8 = Post(title='hi8', content='test3', user_id= 3)

# Add new objects to session
db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8])

# Add tags
t1 = Tag(name='sports')
t2 = Tag(name='food')
t3 = Tag(name='clothing')
t4 = Tag(name='arts')

# Add new tags to session
db.session.add_all([t1,t2,t3,t4])

# Commit posts and tags
db.session.commit()

# Add posts_tags
r1= PostTag(post_id='1', tag_id='4')
r2= PostTag(post_id='2', tag_id='4')
r3= PostTag(post_id='2', tag_id='3')
r4= PostTag(post_id='2', tag_id='1')

# Add new relationships to session
db.session.add_all([r1,r2,r3,r4])

db.session.commit()
