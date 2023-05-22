from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
                    ValidationError, SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from web.models import User, Role


class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1,128)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
   
    ## TODO: get choices from database
    
    role = SelectField('Role')
    # role = SelectField('Role', choices=[('1','Admin'), ('2','Data Scientist'), ('3','Doctor')])
    submit = SubmitField('Create')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use')
        
class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1,128)])
    password = PasswordField('Password')
    password2 = PasswordField('Repeat Password', validators=[EqualTo('password')])
    role = SelectField('Role')
    submit = SubmitField('Update')


class RoleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1,64)])
    description = StringField('Description')
    submit = SubmitField('Create')
    
    def validate_role(self, role):
        role = Role.query.filter_by(title=role.data).first()
        if role is not None:
            raise ValidationError('Role already exists')