from flaskr import app, dbConnection, bcrypt, login_manager
from flask import render_template, url_for, redirect, flash, request
from flaskr.checkPoints_graduation.calculatePoints import getAllPointsDict
from flaskr.forms import Registrator, specChoices, programChoices
from flaskr.DataBaseConnection import User
from flask_login import login_user, logout_user, login_required
#from checkPoints_graduation import DataBaseConnection, pandas, dbConnection
#from flaskr.forms import courseField
@app.route("/", methods =['GET', 'POST'])
def index():
    data = {}   
    loginForm = Registrator()
    if request.method == 'POST':
        fullname = request.form.getlist('field[]')
        data = getAllPointsDict('M', 'Mekatronik', fullname)
        #return render_template('index.html', data = data, )
        #send_data för att ladda ner excel filer t.ex.
    return render_template('index.html', form = loginForm)


@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/donate")
def donate_page():
    return render_template("donate.html")

@app.route("/ans")
def ans():
    return render_template("ans.html", ans = 4)

@app.route("/register", methods = ["POST", "GET"])
def register_page():
    loginForm = Registrator()
    if loginForm.validate_on_submit():

        condition = dbConnection.insertNewUser(6, loginForm.email_address.data, 

                                                bcrypt.generate_password_hash(loginForm.password.data).decode('utf-8'),
                                                loginForm.firstName.data,
                                                'M',
                                                'Energi')
        if condition:
            flash(f'Registrering funkade')
            return redirect(url_for(('index')))
        else:
            flash(f'Registrering fungerade inte')
    if loginForm.errors != {}:
        for err_msg in loginForm.errors.values():
            flash(f'There was an error with creating a user {err_msg}', category = 'danger')
    return render_template('register.html', form = loginForm)


@app.route("/login", methods=["POST", "GET"])
def login_page():
    loginForm = Registrator()
    if loginForm.validate_on_submit():
        df = dbConnection.getUserData()
        df = df.loc[df['userMail'] == loginForm.email_address.data]
        user = User()
        user = user.create_user(df)
        if user:
            if bcrypt.check_password_hash(user.password, loginForm.password.data):
                login_user(user, remember = True)
                return redirect(url_for('about_page'))
    return render_template('login.html', form = loginForm)

@app.route("/forgot", methods=["POST", "GET"])
def forgot_page():
    loginForm = Registrator()
    return render_template('forgotpw.html', form = loginForm)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
