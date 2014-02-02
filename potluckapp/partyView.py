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
    def get(self):
        partyList = PartyModel.retrieve_category()
        return jsonify({
            'success': True,
            'partyList': [{ 'text': item } for item in partyList]
        })
