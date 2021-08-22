from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcryp = Bcrypt()



def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # #configure requests
    # from .requests import configure_requests
    # configure_requests(app)

    #registering blueprints

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    #initializinga extensions

    db.init_app(app)
    bcryp.init_app(app)

    return app