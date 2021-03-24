from flask import Flask
from flaskr import DataBaseConnection
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c88864af30a971bfb83ed19c'
dbConnection = DataBaseConnection.DataBaseConnection()
bcrypt = Bcrypt(app)


from flaskr.routes import *