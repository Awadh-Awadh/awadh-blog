import os


class Config():
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/blog"
   SECRET_KEY = os.environ.get('SECRET_KEY')
   MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
   PASSWORD = os.environ.get('PASSWORD')
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
  

  


class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):
    pass




config_options = {
  'development':DevConfig,
  'production':ProdConfig
}