from flask import request, jsonify, render_template, url_for, redirect
from partyModel import Event, Item
from app import app, db
from forms import CreateEvent, CreateItem
import flask.views
import json

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = CreateEvent()
    if form.validate_on_submit():
        event = Event(name = form.name.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('party', id = event.id, name = event.name))
    return render_template('home.html',
        form = form)

@app.route('/party/<id>_<name>', methods = ['GET', 'POST'])
def party(id, name):  
    form = CreateItem()  
    event = db.session.query(Event).get(id)
    if form.validate_on_submit():
        item = Item(body = form.body.data, person = form.person.data, event_id = event.id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('party', id = event.id, name = event.name))
    form.event_id.data = event.id
    return render_template('party.html',
        event = event,
        form = form)

@app.route('/secondpage')
def secondpage():
    return render_template('secondPage.html')

@app.route('/delete/<item_id>', methods = ['GET', 'POST'])
def delete_item(item_id):
    item = db.session.query(Item).get(item_id)
    event = db.session.query(Event).get(item.event_id)
    db.session.execute('delete from Item where id=' + item_id)
    db.session.commit()
    return redirect(url_for('party', id = event.id, name = event.name))

@app.route('/additem', methods = ['POST'])
def add_item():
    item = Item(event_id=request.form['event_id'], person=request.form['person'], body=request.form['body'])
    event = db.session.query(Event).get(request.form['event_id'])
    db.session.add(item)
    db.session.commit()
    #return jsonify({'event' : event})
    return jsonify(event_id=request.form['event_id'], person=request.form['person'], body=request.form['body'])