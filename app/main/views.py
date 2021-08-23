from app import main
from flask import render_template
from app.requests import get_quotes
from . import main

@main.route('/')
def index():
    










    quotes = get_quotes()

    return render_template('index.html', quotes = quotes)
