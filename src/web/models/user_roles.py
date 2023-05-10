from web import db
from datetime import datetime


class UserRoles(db.Model):
    __tablename__ = 'tbl_users_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id', ondelete='CASCADE'))