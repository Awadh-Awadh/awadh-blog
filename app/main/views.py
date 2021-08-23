from flask_login import login_required
from app import main, db
from flask import render_template,redirect,url_for
from app.requests import get_quotes
from . import main
from .forms import WriteForm
from ..models import User, Posts

@main.route('/')
def index():
    # quotes = get_quotes()

    return render_template('index.html')


@main.route('/publish')
@login_required
def write():
    form = WriteForm()
    if form.validate_on_submit():
        post = Posts(title = form.title.data, conent = form.story.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.account'))
    posts = Posts.query.all()
    return render_template('index.html', form = form, posts = posts)

@main.route('/account')
def account():

    return render_template('account.html')