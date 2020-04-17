from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/")
def home():
    return render_template('home.html', title="Home", sidebar=True)

@main.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='Portfolio', portfolio=True)

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', title='Blog',posts=posts, sidebar=True)
