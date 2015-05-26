# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from flask.ext.sqlalchemy import SQLAlchemy

# configuration


#application
app = Flask(__name__)
app.config.from_object('config.py')
# Use instead of from_object?
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)





if __name__ == '__main__':
    app.run()





