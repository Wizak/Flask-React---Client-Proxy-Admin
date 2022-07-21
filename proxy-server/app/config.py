class Config:
    SECRET_KEY = 'Q6A3hpmZt7'
    DEBUG = False
    SERVER_NAME = '127.0.0.1:6000'


class Develop(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:6001'