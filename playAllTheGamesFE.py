from flask import Flask
from flask_bootstrap import Bootstrap

def username_form(Form):


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    
    @app.route('/')
    def index():

	    form = ExampleForm()
    return app
