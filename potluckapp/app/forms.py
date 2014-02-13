from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, HiddenField
from wtforms.validators import Required, Length
from app.partyModel import Event, Item

class CreateEvent(Form):
    name = TextField('name', validators = [Required(), Length(max=64)])

class CreateItem(Form):
    body = TextField('body', validators = [Required(), Length(max=40)])
    category = TextField('category')
    person = TextField('person', validators = [Required(), Length(max=40)])
    event_id = HiddenField('event_id', validators = [Required()])
