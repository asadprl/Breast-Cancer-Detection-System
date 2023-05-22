from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from . import manage
from .. import db
from web.models import User, Role
from .forms import NewUserForm, RoleForm, EditUserForm

@manage.route('/')
def index():
    return render_template('manage.html')

@manage.route('/users')
def users():
    users =  User.query.all()
    return render_template('users.html', users=users)


@manage.route('/users/create', methods=['GET', 'POST'])
# @login_required
def create_user():
    form = NewUserForm()
    roles = [(role.id, role.title) for role in Role.query.all()]
    form.role.choices = roles
    if form.validate_on_submit():
        user = User(username=form.username.data.lower(),
                    full_name=form.full_name.data,
                    password=form.password.data,
                    role_id=form.role.data
                    )
        db.session.add(user)
        db.session.commit()
        flash(f'User "{user.username} created successfully!')
        return redirect(url_for('manage.users'))
    return render_template('create_user.html', title='Create New User', form=form)

@manage.route('/users/edit/<user>', methods=['GET', 'POST'])
def edit_user(user):
    user_data = User.query.filter(User.username==user).first()
    form = EditUserForm()
    form.username.data = user_data.username
    form.full_name.data = user_data.full_name
    roles = [(role.id, role.title) for role in Role.query.all()]
    form.role.choices = roles
    
    return render_template('edit_user.html', form=form)

@manage.route('/users/delete/<user>', methods=['POST'])
def delete_user(user):
    user_to_del = User.query.filter_by(username=user).first()
    db.session.remove(user_to_del)
    db.session.commit()
    
@manage.route('/roles')
def roles():
    roles = Role.query.all()
    return render_template('roles.html', roles=roles)

@manage.route('/roles/create', methods=['GET', 'POST'])
def create_role():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(title = form.title.data,
                    description=form.description.data
                    )
        db.session.add(role)
        db.session.commit()
        flash(f'Role "{role.title} created successfully!')
        return redirect(url_for('manage.roles'))
    return render_template('create_role.html', title='Create New Role', form=form)

@manage.route('/roles/edit_role/<role>')
def edit_role(role):
    pass

@manage.route('/roles/delete_role/<role>')
def delete_role(role):
    pass

@manage.route('/permissions')
def permissions():
    return render_template('roles.html')