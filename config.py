import os
import secrets


basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")

class Config:
    SECRET_KEY= secrets.token_bytes(16)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    
class Development(Config):
    SQLALCHEMY_DATABASE_URI=f'postgresql://postgres:admin@localhost/flask_contacts'
    Debug=True
    

class Testing(Config):
    SQLALCHEMY_DATABASE_URI=f"sqlite:////{basedir}"


config = {
    'development': Development,
    'testing': Testing
}