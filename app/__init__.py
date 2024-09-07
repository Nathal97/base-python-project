# from flask import Flask

# app = Flask(__name__)

# from app import routes  # Importation des routes 
from flask import Flask
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    
    # Initialiser les routes
    init_routes(app)

    return app
