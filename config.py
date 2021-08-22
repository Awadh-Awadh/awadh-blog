import os


class Config():
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/blog"


class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):
    pass




config_options = {
  'development':DevConfig,
  'production':ProdConfig
}