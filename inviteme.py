#!/usr/bin/env python

""" inviteme.py - A small Flask app to accept emails via POST request
and stores to database. Used for collecting emails. """

from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, jsonify, flash

from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, validators


# Configuration
DEBUG = True
DB_URI = 'sqlite:////tmp/test.db'



### DO NOT EDIT UNDER THIS LINE (unless you know what you're doing) ###

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.secret_key = 'random'
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
class InviteForm(Form):
    email = TextField('Email', [validators.Length(min=6, max=25),
                                validators.Required(),
                                validators.Email()])

# Routes and Views
@app.route("/")
def index():
    form = InviteForm(request.form)


    return render_template('form.html', form=form) 

@app.route("/invite", methods=['POST'])
def invite():
    """ Invite Controller """
    form = InviteForm(request.form)

    if request.method == 'POST' and form.validate():
        query = User.query.filter_by(email=form.email.data).first()
        
        if query == None:
            user = User(form.email.data)
            db.session.add(user)
            db.session.commit()
        else:
            flash('Email is already registered')
            return redirect(url_for('index'))

        print User.query.all()

        flash('Thank you. You will receive an email when invites are ready.')
        return redirect(url_for('index'))
    errors = form.errors
    return render_template('form.html', form=form, errors=errors)


# Return a Flask app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=DEBUG)
