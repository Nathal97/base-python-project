# from flask import Flask

# app = Flask(__name__)

# from app import routes  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .controllers import init_routes


# instance de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Config bdd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init bdd
    db.init_app(app)

    # Init routes
    init_routes(app)

    return app
