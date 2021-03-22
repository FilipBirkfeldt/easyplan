from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form


class courseField(FlaskForm):
    course = StringField(label = 'Kurskod')

class courseList(FlaskForm):
    courseList = FieldList(FieldList(courseField), min_entries = 1)
    submit = SubmitField('Beräkna')