from flask import Flask

from partyView import PartyView, PartyAdd, PartyRetrieve

app = Flask(__name__)

app.add_url_rule('/', view_func=PartyView.as_view('party_view'),
    methods=['GET'])
app.add_url_rule('/partyAdd', view_func=PartyAdd.as_view('party_add'),
    methods=['POST'])
app.add_url_rule('/partyRetrieve/<int:n>',
    view_func=PartyRetrieve.as_view('party_retrieve'), methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
