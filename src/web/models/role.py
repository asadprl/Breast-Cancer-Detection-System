from web import db
from datetime import datetime   

class Role(db.Model):
    __tablename__ = 'tbl_roles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)
       
    def __repr__(self):
        return f'<Role {self.title}>'