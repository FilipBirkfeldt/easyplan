from flaskr import app
from flaskr.DataBaseConnection import User
from flask import flask_login

# https://developers.google.com/gmail/api/quickstart/python - inställningar för GMAIL-API
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

import email
import smtplib 
import ssl
from datetime import date, datetime
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ResetPassword(): 
    "Resets the passWord for the user"
    def init(self):
        self.password = 'eZzzPlAan1231!'
        self.sender_email = 'ezzzPlan@gmail.com'
        self.rec_email = 'lukas.andersson.0210@student.lu.se'
        self.client_id = '687837284079-ekpe5to2r2r1put9uvo43u26laaaim0o.apps.googleusercontent.com'
        self.client_secret = 'miCyIGk4anHsT0E3NJqON4Yw'

    def sendResetPassword(self, userEmail): 

        # MAIL-CONTENT
        subject = "EasyPlan - Reset Password."
        body = '''
        Dear user, 

        We will now reset you password.
        Remeber easy planning is king

        Best regards, 
        Dev-Team at easyplan

        '''

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = rec_email
        message["Subject"] = subject
        # message["Bcc"] = rec_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Create a secure SSL context
        context = ssl.create_default_context()

        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        port = 465  # For SSL
        server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, userEmail, text)
