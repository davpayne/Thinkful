from flask import request, jsonify, render_template
from partyModel import PartyModel

import flask.views
import json

RETRIEVE_DEFAULT_NR = 5

class PartyView(flask.views.MethodView):
    def get(self):
        return render_template('main.html')

class PartyAdd(flask.views.MethodView):
    def post(self):
        args = json.loads(request.data)
        PartyModel.add_item(args['item'])
        return jsonify({ 'success': True })

class PartyRetrieve(flask.views.MethodView):
    def get(self, n):
        try:
            n = int(n)
        except ValueError:
            n = RETRIEVE_DEFAULT_NR
        if n <= 0:
            n = RETRIEVE_DEFAULT_NR
        partyList = PartyModel.retrieve_category(n)
        return jsonify({
            'success': True,
            'partyList': [{ 'text': item } for item in partyList]
        })
