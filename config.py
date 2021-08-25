import os


class Config():
   
   SECRET_KEY = os.environ.get('SECRET_KEY')
   MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
   PASSWORD = os.environ.get('PASSWORD')
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 465
   MAIL_USE_SSL = True
  

  


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/blog"
    DEBUG = True



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
           SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)




config_options = {
  'development':DevConfig,
  'production':ProdConfig
}