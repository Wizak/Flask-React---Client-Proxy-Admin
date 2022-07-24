from flask import request
from flask import jsonify
from flask import current_app
from flask_restful import Resource

from . import api_api
from app import socket_io


@api_api.resource('/receiver')
class StateData(Resource):
    def post(self):
        token = request.args.get('token')
        config_token = current_app.config['SECRET_KEY']
        if token == config_token:
            data = request.get_json()
            if 'end_user_id' in data and 'web_page_url' in data:
                socket_io.emit('receive_message', data, broadcast=True)
                return jsonify(data)
            return {'msg': 'invalid data'}, 412
        return {'msg': 'invalid token'}, 401
