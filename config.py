import os


class Config():
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/blog"
   SECRET_KEY = os.environ.get('SECRET_KEY')
   MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
   PASSWORD = os.environ.get('PASSWORD')
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 465
   MAIL_USE_SSL = True
  

  


class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):
    pass




config_options = {
  'development':DevConfig,
  'production':ProdConfig
}