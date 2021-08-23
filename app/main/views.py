from flask_login import login_required
from app import main
from flask import render_template
from app.requests import get_quotes
from . import main
from .forms import WriteForm

@main.route('/')
def index():
    # quotes = get_quotes()

    return render_template('index.html')


@main.route('/publish')
@login_required
def write():
    form = WriteForm()
    return render_template('write.html', form = form)

