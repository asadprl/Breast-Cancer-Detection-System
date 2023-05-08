from web import app
from flask import render_template, redirect, url_for
from flask_login import current_user

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', greet=current_user.username)
    else:
        return redirect(url_for('auth.login'))