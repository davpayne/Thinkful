from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    items = db.relationship('Item', backref = 'event', lazy = 'dynamic')

    def __repr__(self):
        return '<Event %r>' % (self.name) 

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    category = db.Column(db.String(20))
    person = db.Column(db.String(140))

    def __repr__(self): 
        return '<Post %r>' % (self.body)