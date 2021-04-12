# -*- coding: utf-8 -*-

from home.view import home
from flask import Flask, Blueprint

app = Flask(__name__)

""" Register blueprint's """
app.register_blueprint(home)

""" Config """
app.config.update(
    DEBUG = True,
    SECRET_KEY = "smailhnhdhprhuvfnujfszsav"
)

class Project(object):
    def __init__(self, *args):
        ...