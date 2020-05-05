import os
from flask import render_template, request, Blueprint
from flaskblog.models import Post

subjects = Blueprint('subjects', __name__, template_folder='subjects_templates', url_prefix='/subjects', static_folder='static')

@subjects.route("/")
def subject_index():
    return render_template('subjects.html', title='view all')


@subjects.route("/<subject_name>")
def subject_home(subject_name):
    return render_template(os.path.join('/' + subject_name + '/' + subject_name + '_home.html'), 
                            subject_name=subject_name, title=subject_name)

#@subjects.route("/subjects/math/calc_i/intro")
#def ():
#    return render_template('subjects/math/calc_I/calc_I_intro.html', title="Calc I", topic=True, topic_name="Calculus I")

#@subjects.route("/subjects/math/calc_i/practice_problems")
#def ():
#    return render_template('subjects/math/calc_I/calc_I_pp.html', title="Calc I - Practice", topic=True, topic_name="Calculus I")