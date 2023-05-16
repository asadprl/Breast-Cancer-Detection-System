from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
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
    
    __create_roles_and_users(app)
    return app

def __create_roles_and_users(app):
    from web.models import User, Role, Permission
    with app.app_context():
        if User.query.filter(User.username=='admin') is None:
            db.create_all()
            p_add_user = Permission(title='add_user')
            p_edit_user = Permission(title='edit_user')
            db.session.add(p_add_user)
            db.session.add(p_edit_user)
            db.session.commit()
            admin_role = Role(title='admin')
            admin_role.permissions.append(p_add_user)
            admin_role.permissions.append(p_edit_user)
            db.session.add(admin_role)
            db.session.commit()
            admin = User(username='admin', full_name='Administrator', password='123', role_id=admin_role.id)
            db.session.add(admin)
            db.session.commit()
    