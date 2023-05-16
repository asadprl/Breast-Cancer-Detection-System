from web import db

class Permission(db.Model):
    __tablename__ = 'tbl_permissions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)

    roles = db.relationship('Role', secondary='roles_permissions')

    def __repr__(self) -> str:
        return f'<Permission {self.title}'