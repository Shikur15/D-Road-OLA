from flask import Flask
from mainapp.config import Config
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# app = Flask(name)
db = SQLAlchemy()
bcrypt =Bcrypt()
login_manager = LoginManager()
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(name)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    # import blueprint
    from mainapp.users.routes import users
    from mainapp.errors.handle_error import errors

    # register blue print
    app.register_blueprint(errors)
    app.register_blueprint(users)

    return app