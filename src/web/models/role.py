from web import db
from datetime import datetime   

class Role(db.Model):
    __tablename__ = 'tbl_roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), nullable=True)

    def __init__(self, id, name, description, 
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.id = id
        self.name = name
        self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        
    def __repr__(self):
        return f'<Role {self.title}>'