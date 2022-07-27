from flask import request
from flask import jsonify
from flask import current_app
from flask_restful import Resource

from . import api_api
from app import socket_io
from app.models import DataBase

from datetime import datetime


@api_api.resource('/receiver')
class StateData(Resource):
    def post(self):
        token = request.args.get('token')
        config_token = current_app.config['SECRET_KEY']
        if token == config_token:
            data = request.get_json()
            if 'end_user_id' in data and 'web_page_url' in data:
                now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                DataBase.set_data({**data, 'date': now})
                return jsonify(data)
            return {'msg': 'invalid data'}, 412
        return {'msg': 'invalid token'}, 401
