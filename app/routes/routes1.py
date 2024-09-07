from flask import Blueprint, render_template

example_route = Blueprint('example_route', __name__)

@example_route.route('/')
def home():
    return render_template('home.html')
