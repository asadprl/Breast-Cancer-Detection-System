from web import db  

class Role(db.Model):
    __tablename__ = 'tbl_roles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)

    users = db.relationship('User', backref='role')
    permissions = db.relationship('Permission', back_populates='roles', secondary='roles_permissions')

    def has_permission(self, permission):
        return self.permissions
       
    def __repr__(self):
        return f'<Role {self.title}>'