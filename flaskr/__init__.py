from flask import Flask
from flaskr import DataBaseConnection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c88864af30a971bfb83ed19c'
dbConnection = DataBaseConnection.DataBaseConnection()


from flaskr.routes import *