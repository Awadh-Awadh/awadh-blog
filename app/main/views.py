from flask_login import login_required, current_user
from app import main, db
from flask import render_template,redirect,url_for, flash
from app.requests import get_quotes
from . import main
from .forms import EditProfile, WriteForm
from ..models import User, Posts

@main.route('/')
def index():
    # quotes = get_quotes()
    posts = Posts.query.all()

    # blogs = [
    #     {
    #         'title':
    #     }
    # ]

    return render_template('index.html', posts = posts)


@main.route('/publish', methods = ['GET','POST'])
@login_required
def write():
    form = WriteForm()
    if form.validate_on_submit():
        post = Posts(title = form.title.data, content = form.story.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.account'))
    posts = Posts.query.all()
    return render_template('write.html', form = form, posts = posts)

@main.route('/account')
def account():


    return render_template('account.html')

@main.route('/profile', methods = ['GET','POST'])
def profile():
    form = EditProfile()
    image_file = url_for('static', filename = 'images/' + current_user.image_url)
    if form.validate_on_submit():
        
        current_user.username = form.user.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Acount updated successfully', 'success')

    form.user.data = current_user.username
    form.bio.data = current_user.bio

    return render_template('userprof.html', form = form, image = image_file)