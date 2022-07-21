from flask import jsonify
from flask import request
from flask_socketio import emit

from app import socket_io


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
