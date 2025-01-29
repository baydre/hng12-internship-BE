from flask import Flask
from flask_cors import CORS

def create_app():
    """
    create flask app
    """
    app = Flask(__name__)
    CORS(app)
    
    from api.basic_info import display_info

    app.register_blueprint(display_info, url_prefix='/')

    return app