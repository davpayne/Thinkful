from app import db
from uuid import uuid4

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    #have to change date time
    #event_date = db.Column(db.String(64))
    #attendees = db.relationship('Attendee', backref= 'author', lazy = 'dynamic')
    #about_me = db.Column(db.String(140))
    #last_seen = db.Column(db.DateTime)

    def __repr__(self):
        return '<Event %r>' % (self.name) 

class PartyModel:
    def __init__(self):
        pass

    @classmethod
    def add_item(cls, item):
        pass
        """_cursor.execute('INSERT INTO party(text) VALUES(?)', (item, ))
        _conn.commit()
"""
    @classmethod
    def retrieve_category(cls):
        pass
        """rows = _cursor.execute(
            'SELECT text FROM party ORDER BY id DESC LIMIT ?', (n, )
        )
        return [r['text'] for r in rows]"""
