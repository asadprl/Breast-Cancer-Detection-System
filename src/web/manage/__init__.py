from flask import Blueprint

manage = Blueprint('manage', __name__, template_folder='templates', url_prefix='/manage')

from . import views