from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def __register_blueprints(app:Flask):
    from web.auth import auth
    from web.main import main
    
    app.register_blueprint(auth)
    app.register_blueprint(main)

def create_app(config_name:str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    __register_blueprints(app)
    
    
    return app
    