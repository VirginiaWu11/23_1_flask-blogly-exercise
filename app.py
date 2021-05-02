"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash, session
from models import db, connect_db, User
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

@app.route('/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('userdetail.html',user=user)

@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edituser.html',user=user)

@app.route('/<int:user_id>/edit', methods=['POST'] )
def edit_user_post(user_id):
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


@app.route('/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    flash(f"User {user.first_name} deleted!", 'danger')
    return redirect('/')