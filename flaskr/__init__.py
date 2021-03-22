from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c88864af30a971bfb83ed19c'

from flaskr.routes import *