
import os
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

class Config:
    SECRET_KEY = os.urandom(32)
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://helana:1993@localhost:5432/book_store'
    UPLOADED_PHOTOS_DEST = 'app/static/'


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}