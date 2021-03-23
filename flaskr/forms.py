from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form


class courseField(FlaskForm):
    course = StringField(label = 'Kurskod')
    submit = SubmitField(label = 'Let us count')

class courseList(FlaskForm):
    courseList = FieldList(FieldList(courseField), min_entries = 1)
    submit = SubmitField('Beräkna')


class User(FlaskForm):
    name = StringField(label = 'Name', nullable = False, unique = False)
    email_address = StringField(label = 'Email Adress', nullable = False, unique = True)
    password = StringField(label = 'Password')