from flask import Flask
from flaskr import DataBaseConnection
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'c88864af30a971bfb83ed19c'
dbConnection = DataBaseConnection.DataBaseConnection()
bcrypt = Bcrypt(app)


from flaskr.routes import *