from flaskr import app, dbConnection, bcrypt, login_manager
from flask import render_template, url_for, redirect, flash, request, jsonify
from flaskr.checkPoints_graduation.calculatePoints import getAllPointsDict
from flaskr.forms import Registrator, specChoices, programChoices, loginForm, ProgramsForm
from flaskr.DataBaseConnection import User
from flask_login import login_user, logout_user, login_required
#from checkPoints_graduation import DataBaseConnection, pandas, dbConnection
#from flaskr.forms import courseField
@app.route("/", methods =['GET', 'POST'])
def index():
    programs=ProgramsForm()
    programs.program.choices
    programs.spec.choices = [(spec.id, spec.name) for spec in Spec.query.filter_by(program='M').all()]
    if request.method == 'POST':
        spec = Spec.query.filter_by(id=programs.spec.data).first()
        return 'Program: {}, Specialization: {}'.format(programs.program.data, spec.name)
    

    return render_template('index.html', programs=programs)

@app.route("/specialization/<program>")
def specialization(program):
    specializations = Spec.query.filter_by(program=program).all()

    specializationArray = []

    for spec in specializations:
        specializationObj = {}
        specializationObj['id'] = spec.id
        specializationObj['name'] = spec.name
        specializationArray.append(specializationObj)
    return jsonify({'specializations' : specializationArray})


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
    registerForm = Registrator()
    if registerForm.validate_on_submit():

        condition = dbConnection.insertNewUser(6, registerForm.email_address.data, 
                                                bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8'),
                                                registerForm.firstName.data,
                                                'M',
                                                'Energi')
        if condition:
            flash(f'Registrering funkade')
            return redirect(url_for(('index')))
        else:
            flash(f'Registrering fungerade inte')
    if registerForm.errors != {}:
        for err_msg in registerForm.errors.values():
            flash(f'There was an error with creating a user {err_msg}', category = 'danger')
    return render_template('register.html', form = registerForm)


@app.route("/login", methods=["POST", "GET"])
def login_page():
    logForm = loginForm()
    if logForm.validate_on_submit():
        df = dbConnection.getUserData()
        df = df.loc[df['userMail'] == logForm.email_address.data]
        user = User()
        user.create_user(df)
        if not df.empty:
            if bcrypt.check_password_hash(user.password , logForm.password.data):
                login_user(user, remember = True)
                return redirect(url_for('about_page'))
            else:
                flash(f'Wrong password')
        else:
            flash(f'No such user')
    if logForm.errors != {}:
        for err_msg in logForm.errors.values():
            flash(f'Error {err_msg}', category = 'danger')
    return render_template('login.html', form = logForm)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('about_page'))

@app.route("/forgot", methods=["POST", "GET"])
def forgot_page():
    loginForm = Registrator()
    return render_template('forgotpw.html', form = loginForm)

@login_manager.user_loader
def load_user(user_id):
    df = dbConnection.getUserData()
    df = df.loc[df['userMail'] == user_id]
    user = User()
    user.create_user(df)
    return user
