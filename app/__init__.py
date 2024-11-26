from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import User
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'db.sqlite')}"

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints or routes here
    from app.routes import main
    app.register_blueprint(main)

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Retrieve the user from the database by their ID


    return app