from flask import request
from flask import jsonify
from flask import current_app
from flask_restful import Resource
import time

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
                data1 = f"end_user_id: {data['end_user_id']}"
                data2 = f"web_page_url: {data['web_page_url']}"
                socket_io.emit('receive_id', data1)
                time.sleep(0.2)
                socket_io.emit('receive_url', data2)
                return jsonify(data)
            return {'msg': 'invalid data'}, 412
        return {'msg': 'invalid token'}, 401
