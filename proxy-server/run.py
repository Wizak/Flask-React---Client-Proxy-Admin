from weakref import proxy
from app import create_app
from app import socket_io


if __name__ == '__main__':
    proxy_app = create_app()
    socket_io.run(proxy_app)
