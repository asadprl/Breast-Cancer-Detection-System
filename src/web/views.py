from web import app
from flask import render_template, redirect, url_for
from flask_user import login_required, roles_required, current_user

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', greet=current_user.full_name)
    else:
        return redirect(url_for('auth.login'))

@app.route('/members')
@login_required
def member_page():
    return 'members area'

@app.route('/admin')
@roles_required('Admin')
def admin_page():
    return 'admin area'
