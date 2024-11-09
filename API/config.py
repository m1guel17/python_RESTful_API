import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "KEYSSS"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///DATABASE.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False