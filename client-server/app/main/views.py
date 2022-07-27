from flask import render_template
from flask import jsonify
from flask import request

from . import main_bp


@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('home.html')


@main_bp.route('/show')
def show():
    return render_template('show.html')


@main_bp.route('/login')
def login():
    return render_template('login.html')


@main_bp.route('/register')
def register():
    return render_template('register.html')


def page_error(e):
        return render_template('error404.html'), 404
