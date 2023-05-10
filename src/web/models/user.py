from web import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_user import UserManager, UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'tbl_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    # role = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), nullable=True)

    roles = db.relationship('Role', secondary='tbl_users_roles')

    def __init__(self, id, username, full_name, password, #role, 
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.set_password(password)
        # self.role = role
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        
        
        
    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

from web import app
user_manager = UserManager(app, db, User)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))