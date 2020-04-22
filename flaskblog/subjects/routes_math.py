from flask import render_template, request, Blueprint
from flaskblog.models import Post

math = Blueprint('math', __name__)


@math.route("/subjects/math")
def math_home():
    return render_template('/subjects/math/math_home.html', title="Math Home", math=True , subject_name="Mathematics")

@math.route("/subjects/math/calc_i/intro")
def calc_i_intro():
    return render_template('subjects/math/calc_I/calc_I_intro.html', title="Calc I", topic=True, topic_name="Calculus I")

@math.route("/subjects/math/calc_i/practice_problems")
def calc_i_pp():
    return render_template('subjects/math/calc_I/calc_I_pp.html', title="Calc I - Practice", topic=True, topic_name="Calculus I")