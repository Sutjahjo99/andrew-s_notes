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

@subjects.route("/<subject_name>/<topic_name>")
def subject_topic(subject_name, topic_name):
    return render_template(os.path.join('/' + subject_name + '/' + topic_name + '/' + topic_name + '_index.html'),
                            subject_name=subject_name, topic_name=topic_name, title=topic_name, sidebar=True, topic=True)

@subjects.route("/<subject_name>/<topic_name>/<chapter>/<num>")
def topic_chapter(subject_name, topic_name, chapter, num):
    return render_template(os.path.join('/' + subject_name + '/' + topic_name + '/' + chapter + '/' + num + '.html'),
                            subject_name=subject_name, topic_name=topic_name, chapter=chapter, num=num, title=topic_name, 
                            sidebar=True, topic=True)

