from flask import Flask
from flask_cors import CORS


from app.config import Develop


def create_app():
    app = Flask(__name__)
    app.config.from_object(Develop)
    
    CORS(app, resources={r"/*":{"origins":"*"}})

    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
