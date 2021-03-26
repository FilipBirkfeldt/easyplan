from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form, PasswordField, SelectField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from flaskr import dbConnection
specChoices = [('Mek', 'Mekatronik'), ('Energi', 'Energi'), ('Log','Logistik')]
programChoices = [('M', 'Maskinteknik')]

class courseField(FlaskForm):
    course = StringField(label = 'Kurskod')
    submit = SubmitField(label = 'Let us count')

class courseList(FlaskForm):
    courseList = FieldList(FieldList(courseField), min_entries = 1)
    submit = SubmitField('Beräkna')


class Registrator(FlaskForm):
   # def __init__(self):
    #    super(Registrator, self).__init__()
    #    self.dbConnection = dbConnection

    def validate_email_address(self, email_address_to_check):
        condition = dbConnection.ifNew_UserEmail(email_adress_to_check.data)
        if not condition:
            raise ValidationError('Email address already in use')

    firstName = StringField(label = 'First Name', validators = [DataRequired(), Length(min = 2, max = 20)])
    lastName = StringField(label = 'Last Name', validators = [DataRequired(), Length(min = 2, max = 20)])
    email_address = StringField(label = 'Email Adress', validators = [Email(message = 'Please enter a valid email address'), DataRequired()])
    password = PasswordField(label = 'Password', validators = [Length(min = 3, max = 15, message = 'Password must be between %(min)d and %(max)d characters'),
                                                                DataRequired( message = "Please enter a password")])
    passwordConfirmation = PasswordField(label = 'Confirm password', validators = [EqualTo('password', message = 'Password does not match, make sure password is case-sensitive')
                                                                                    ,DataRequired(message = "Please re-enter password")])
    #program = SelectField(label = 'Program', choices = programChoices, default='M')
    #specialisering = SelectField(label = 'Specialisering',  choices = specChoices, default='Mekatronik')

class loginForm(FlaskForm):

    email_address = StringField(label = 'Email Adress', validators = [Email(message = 'Please enter a valid email address'), DataRequired()])
    password = PasswordField(label = 'Password', validators = [Length(min = 3, max = 15, message = 'Password must be between %(min)d and %(max)d characters'),
                                                                DataRequired( message = "Please enter a password")])

<<<<<<< HEAD
class forgotPwForm(FlaskForm):

    def validate_email_address(self, email_address_to_check):
        dfInfo = dbConnection.getUserData()
        dfInfo = dfInfo.loc[[dfInfo['userMail'] == email_address_to_check]]
        if dfInfo.empty:
            raise ValidationError('No such email address exists, please try again.')
    email_address = StringField(label = 'Email Adress', validators = [Email(message = 'Please enter a valid email address'), DataRequired()])
=======

class ProgramsForm(FlaskForm):
    program = SelectField('Program', choices=[('D','Datateknik'), ('W','Ekosystemteknik'), ('E','Elektroteknik'), ('I','Industriell Ekonomi'), ('K','Kemiteknik'), ('L','Lantmäteri'),
                                                ('M','Maskinteknik'), ('TD','Maskinteknik - Teknisk Design'), ('BME','Medicin och Teknik'), ('F','Teknisk Fysik'), ('Pi','Teknisk Matematik'), 
                                                    ('N','Teknisk nanovetenskap'), ('V','Väg- och vattenbyggnad')])
    spec = SelectField('Specialization', choices=[])
>>>>>>> d448e77d379ca2fdb7a26c2f15408120082a764a
