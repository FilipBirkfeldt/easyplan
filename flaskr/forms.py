from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form, PasswordField
from wtforms.validators import Length, EqualTo, DataRequired, Email


class courseField(FlaskForm):
    course = StringField(label = 'Kurskod')
    submit = SubmitField(label = 'Let us count')

class courseList(FlaskForm):
    courseList = FieldList(FieldList(courseField), min_entries = 1)
    submit = SubmitField('Beräkna')


class Registrator(FlaskForm):

    def validate_email_address(self, email_adress_to_check):
        pass

    FirstName = StringField(label = 'Name', validators = [DataRequired, Length(min = 2, max = 20)])
    LastName = StringField(label = 'Name', validators = [DataRequired, Length(min = 2, max = 20)])
    email_address = StringField(label = 'Email Adress', validators = [Email(), DataRequired ])
    password = PasswordField(label = 'Password', validators = [Length(min = 3, max = 15)])
    passwordConfirmation = PasswordField(label = 'Confirm password', validators = [EqualTo(password)])
