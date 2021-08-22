from flask import render_template, redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User,Posts
from .. import db,bcrypt
from flask_login import login_user,current_user, logout_user,login_required


@auth.route('/register')
def register():
  if current_user.is_authenticated:
      return redirect('main.index')
  form = RegisterForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data)
      user = User(username = form.username.data, email = form.email.data, password = hashed_password)
      db.session.add(user)
      db.session.commit()
      return redirect('auth.login')
  render_template('auth/register.html', form=form)



  @auth.route('/login')
  def login():
    if current_user.is_authenticated:
      return redirect('main.index')
    form = LoginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(email = form.email.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', form = form)

  @auth.route('/logout')
  @login_required
  def logout():
      logout_user()