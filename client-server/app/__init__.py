from flask import Flask
from flask import render_template
from flask_cors import CORS

from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app, resources={r"/*":{"origins":"*"}})

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.main.views import page_error
    app.register_error_handler(404, page_error)

    return app
