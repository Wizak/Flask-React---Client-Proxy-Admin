from sqlite3 import Date
from flask import jsonify
from flask import request
from flask_socketio import emit, send

from app import socket_io
from app.models import DataBase


@socket_io.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print('Client has connected')
    emit('connect', {'data': f'id: {request.sid} is connected'})


@socket_io.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print(request.sid)
    print('Client disconnected')
    emit('disconnect', f'client {request.sid} disconnected', broadcast=True)


@socket_io.on("remote-call")
def send_data(client_data):
    """event listener when client does calling to the server"""
    print(client_data)
    if client_data['action'] == 'GET_LIST':
        if client_data['collection'] == 'visitors':
            client_payload = client_data['payload']
            pagination = client_payload['pagination']
            sorting = client_payload['sort']

            body = DataBase.get_data()
            pag_body, total = DataBase.pag_data(body, pagination)
            sort_body = DataBase.sort_data(pag_body, sorting)

            return {'data': sort_body, 'total': total}
    raise Exception('Not implemented')
