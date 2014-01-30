from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from partyView import PartyView, PartyAdd, PartyRetrieve

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your-username:your-password@localhost/development'
#db = SQLAlchemy(app)

app.add_url_rule('/', view_func=PartyView.as_view('party_view'),
    methods=['GET'])
app.add_url_rule('/partyAdd', view_func=PartyAdd.as_view('party_add'),
    methods=['POST'])
app.add_url_rule('/partyRetrieve/<int:n>',
    view_func=PartyRetrieve.as_view('party_retrieve'), methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
