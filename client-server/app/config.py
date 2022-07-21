class Config:
    SECRET_KEY = 'ELrQ5rf6fT'
    DEBUG = False
    SERVER_NAME = '127.0.0.1:5000'


class Develop(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:5001'