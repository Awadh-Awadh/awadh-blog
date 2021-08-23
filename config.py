import os


class Config():
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/blog"
   SECRET_KEY = os.environ.get('SECRET_KEY')


class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):
    pass




config_options = {
  'development':DevConfig,
  'production':ProdConfig
}