from flask import render_template, request, Blueprint
from flaskblog.models import Post

cheme = Blueprint('cheme', __name__)


@cheme.route("/subjects/cheme")
def cheme_home():
    return render_template('/subjects/cheme/cheme_home.html', title="Cheme Home", sidebar=True, sb_ann=True, subject_name="Chem. Eng.")
