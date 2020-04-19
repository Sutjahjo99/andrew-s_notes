from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flaskblog.config import Config


db = SQLAlchemy()
admin = Admin()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.admin.routes import admins
    from flaskblog.subjects.routes_chem import chem
    from flaskblog.subjects.routes_cheme import cheme
    from flaskblog.subjects.routes_math import math
    from flaskblog.subjects.routes_phys import phys
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(admins)
    app.register_blueprint(chem)
    app.register_blueprint(cheme)
    app.register_blueprint(math)
    app.register_blueprint(phys)

    return app