from flask import render_template, request, Blueprint
from flaskblog.models import Post

math = Blueprint('math', __name__)


@math.route("/subjects/math")
def math_home():
    return render_template('/subjects/math/math_home.html', title="Math Home", subject=True , subject_name="Mathematics")
