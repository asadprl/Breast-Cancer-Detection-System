from flask import render_template, redirect, url_for
from flask_login import current_user
from . import main
from .. import db


@main.route('/')
def index():
    return render_template('index.html')