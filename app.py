"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash, session
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_home():
    return redirect('/users')

@app.route('/users')
def users_list():
    users = User.query.all()
    return render_template('users.html',users=users)

@app.route('/users/new')
def new_user():
    return render_template('newuser.html')

@app.route('/users/new', methods=['POST'])
def add_user():
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    image_url= request.form['img_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    flash(f"User {new_user.first_name} added!", 'success')

    return redirect(f'/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('userdetail.html',user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edituser.html',user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'] )
def edit_user_profile(user_id):
    user = User.query.get_or_404(user_id)
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    image_url= request.form['img_url']

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()

    flash(f"User {user.first_name} updated!", 'success')

    return redirect(f'/users')


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    flash(f"User {user.first_name} deleted!", 'danger')
    return redirect('/')


# ------------ Post Routes

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('newpost.html',user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def submit_new_post(user_id):
    title = request.form['title']
    content = request.form['content']
    
    post= Post(title=title, content=content, user_id=user_id)

    db.session.add(post)
    db.session.commit()
    flash(f"New Post, {post.title}, added!", 'success')

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('/postdetail.html',post=post)

@app.route('/posts/<int:post_id>/edit' )
def edit_post_form(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('editpost.html',post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'] )
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    title= request.form['title']
    content= request.form['content']

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()

    flash(f'Post "{post.title}" updated!', 'success')

    return redirect(f'/posts/{post_id}')



@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = post.users.id
    Post.query.filter_by(id=post_id).delete()

    db.session.commit()
    flash(f'Post "{post.title}"" by {post.users.first_name} {post.users.last_name} has been deleted!', 'danger')

    return redirect(f'/users/{user_id}')