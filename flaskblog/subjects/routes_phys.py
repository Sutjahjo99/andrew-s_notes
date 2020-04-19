from flask import render_template, request, Blueprint
from flaskblog.models import Post

phys = Blueprint('phys', __name__)


@phys.route("/subjects/physics")
def phys_home():
    return render_template('/subjects/phys/phys_home.html', title="Physics Home", sidebar=True, sb_ann=True, subject_name="Physics")
