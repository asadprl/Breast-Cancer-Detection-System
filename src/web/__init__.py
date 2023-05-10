from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


from web import views, models
with app.app_context():
    db.create_all()
    
    #for testing
    from web.models import User, Role
    if not User.query.filter(User.username=='admin').first():
        user = User(None,'admin','Admin User 1','123')
        user.roles.append(Role(None,'Admin','Admin Role'))
        db.session.add(user)
        db.session.commit()
