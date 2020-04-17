from flask import render_template, request, Blueprint
from flaskblog import db, login_manager, admin
from flask_login import current_user, login_required


admins = Blueprint('admins', __name__)

@admins.route("/admin")
@login_required
def admin():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))