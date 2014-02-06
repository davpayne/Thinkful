from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from app.partyModel import Event, Item

class CreateEvent(Form):
    name = TextField('name', validators = [Required()])

class CreateItem(Form):
    body = TextField('body', validators = [Required()])
    category = TextField('category')
    person = TextField('person', validators = [Required()])
