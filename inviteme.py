#!/usr/bin/env python

""" inviteme.py - A small Flask app to accept emails via POST request
and stores to database. Used for collecting emails. """

from flask import Flask
from flask import render_template, redirect, url_for
from flask import request

from flask.ext.sqlalchemy import SQLAlchemy


# Configuration



### DO NOT EDIT UNDER THIS LINE (unless you know what you're doing) ###

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# DB Model
class User(db.Model):
    __tablename__ = 'User'
    email = db.Column(db.String(120), primary_key=True, unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.email

# Form Model

# Routes and Views
@app.route("/")
def index():


    return render_template('form.html') 

@app.route("/invite", methods=['POST'])
def invite():
    """ Invite Controller """

    email = request.form['email']
    print email

    user = User(email)
    db.session.add(user)
    db.session.commit()

    print User.query.all()

    return redirect(url_for('index'))


# Return a Flask app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
