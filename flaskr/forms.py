from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form, PasswordField, SelectField
from wtforms.validators import Length, EqualTo, DataRequired, Email
specChoices = [('Mek', 'Mekatronik'), ('Energi', 'Energi'), ('Log','Logistik')]
programChoices = [('M', 'Maskinteknik')]

class courseField(FlaskForm):
    course = StringField(label = 'Kurskod')
    submit = SubmitField(label = 'Let us count')

class courseList(FlaskForm):
    courseList = FieldList(FieldList(courseField), min_entries = 1)
    submit = SubmitField('Beräkna')


class Registrator(FlaskForm):

    #def validate_email_address(self, email_adress_to_check):
    #    pass

    firstName = StringField(label = 'First Name', validators = [DataRequired(), Length(min = 2, max = 20)])
    lastName = StringField(label = 'Last Name', validators = [DataRequired(), Length(min = 2, max = 20)])
    email_address = StringField(label = 'Email Adress', validators = [Email(message = 'Please enter a valid email address'), DataRequired() ])
    password = PasswordField(label = 'Password', validators = [Length(min = 3, max = 15, message = 'Password must be between %(min)d and %(max)d characters')])
    passwordConfirmation = PasswordField(label = 'Confirm password', validators = [EqualTo('password', message = 'Password does not match, make sure password is case-sensitive')])
    program = SelectField(label = 'Program', choices = programChoices, validators = [DataRequired()])
    specialisering = SelectField(label = 'Specialisering',  choices = specChoices, validators = [DataRequired()])
    submit = SubmitField(label = 'Skapa Konto')