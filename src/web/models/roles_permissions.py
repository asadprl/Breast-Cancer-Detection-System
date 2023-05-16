from web import db

class RolesPermissions(db.Model):
    __tablename__ = 'roles_permissions'

    id = db.Column(db.Integer, primary_key=True)

    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('tbl_permissions.id'))
    