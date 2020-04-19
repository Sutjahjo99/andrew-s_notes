from flask import render_template, request, Blueprint
from flaskblog.models import Post

chem = Blueprint('chem', __name__)


@chem.route("/subjects/chemistry")
def chem_home():
    return render_template('/subjects/chem/chem_home.html', title="Chem Home", sidebar=True, sb_ann=True, subject_name="Chemistry")
