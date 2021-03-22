from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList


def courseField(FlaskForm):
    course = StringField(label = 'Kurskod')

def couseList(FlaskForm):
    courseList = FieldList(courseField(), )