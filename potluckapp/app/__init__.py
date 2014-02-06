import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your-username:your-password@localhost/development'

from app import partyModel, partyView
"""
app.add_url_rule('/', view_func=PartyView.as_view('party_view'),
    methods=['GET'])
app.add_url_rule('/partyAdd', view_func=PartyAdd.as_view('party_add'),
    methods=['POST'])
app.add_url_rule('/partyRetrieve/<int:n>',
    view_func=PartyRetrieve.as_view('party_retrieve'), methods=['GET'])
"""
