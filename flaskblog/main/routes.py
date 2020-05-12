from flask import flash, redirect, render_template, request, Blueprint, url_for
from flaskblog.main.forms import ContactForm
from flaskblog.models import Post

from flaskblog.main.utils import send_email

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title="Home", sidebar=True, sb_ann=True, main="True")

@main.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='Portfolio', sidebar=True, sb_port=True, main="True")

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', title='Blog',posts=posts, sidebar=True, sb_ann=True, main="True")

@main.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        useremail = form.email.data
        usertitle = form.title.data
        usermess = form.message.data
        send_email(useremail, usertitle, usermess)
        flash("Your message has been sent! I will get to you as soon as possible!", "success")
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form)
