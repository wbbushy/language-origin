# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/language-origin.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#application
app = Flask(__name__)
app.config.from_object(__name__)
# Use instead of from_object?
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#connct to db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run()
