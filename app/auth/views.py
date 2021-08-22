from flask import render_template
from werkzeug.utils import redirect
from . import auth
from .forms import RegisterForm


@auth.route('/register')
def register():
  form = RegisterForm()
  if form.validate_on_submit():
      return redirect('auth.login')
  render_template('auth/register.html', form=form)