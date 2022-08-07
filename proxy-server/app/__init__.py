from flask import Flask

from flask_cors import CORS
from flask_socketio import SocketIO


from app.config import Config


socket_io = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*":{"origins":"*"}})
    
    socket_io.init_app(app, cors_allowed_origins='*')
    from app.socket import views

    from app.api import api_bp
    app.register_blueprint(api_bp)

    return app
