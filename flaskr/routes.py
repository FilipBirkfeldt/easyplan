from flaskr import app, dbConnection, bcrypt, login_manager
from flask import render_template, url_for, redirect, flash, request, jsonify, Markup
from flaskr.checkPoints_graduation.calculatePoints import getAllPointsDict

from flaskr.forms import Registrator, specChoices, programChoices, loginForm, ProgramsForm, forgotPwForm

from flaskr.DataBaseConnection import User
from flask_login import login_user, logout_user, login_required

import pandas as pd

@app.route("/", methods =['GET', 'POST'])
def index():
    programsForm=ProgramsForm()
    programsForm.spec.choices = dbConnection.getSpecis_from_Program('B')
    if  request.method == 'POST':
        #spec = dbConnection.getSpecis_from_Program(program=programsForm.program.data)
        #return f'Program: {programsForm.program.data}, Specialization: {spec}, Error_MSG {programsForm.errors.values()}'
        courseList = dbConnection.readAllData()
        y1List = courseList[courseList['Typ'] == '1'][['Kursnamn', 'Kurskod', 'Poang']].values
        y2List = courseList[courseList['Typ'] == '2'][['Kursnamn', 'Kurskod', 'Poang']].values
        y3List = courseList[courseList['Typ'] == '3'][['Kursnamn', 'Kurskod', 'Poang']].values
        specList = courseList[courseList['Typ'] == 'Energiteknik'][['Kursnamn', 'Kurskod', 'Poang']].values
        items_spec = {1: {}}
        items_y1 = {1: {}}
        items_y2 = {1: {}}
        items_y3 = {1: {}}
        for i in range(len(specList)):
            items_spec[i] = {}
            items_spec[i]['coursename'] = specList[i][0]
            items_spec[i]['code'] = specList[i][1]
            items_spec[i]['credits'] = specList[i][2]

        for i in range(len(y1List)):
            items_y1[i] = {}
            items_y1[i]['coursename'] = y1List[i][0]
            items_y1[i]['code'] = y1List[i][1]
            items_y1[i]['credits'] = y1List[i][2]
        for i in range(len(y2List)):
            items_y2[i] = {}
            items_y2[i]['coursename'] = y2List[i][0]
            items_y2[i]['code'] = y2List[i][1]
            items_y2[i]['credits'] = y2List[i][2]
        for i in range(len(y3List)):
            items_y3[i] = {}
            items_y3[i]['coursename'] = y3List[i][0]
            items_y3[i]['code'] = y3List[i][1]
            items_y3[i]['credits'] = y3List[i][2]
        
        return render_template('index.html' ,items_spec=items_spec, items_y1=items_y1, 
        items_y2=items_y2, items_y3=items_y3 ,programs=programsForm)

    return render_template('index.html', programs=programsForm)

@app.route("/specialization/<program>")
def specialization(program):

    specList = dbConnection.getSpecis_from_Program(program)

    specializationArray = []

    for idx, key in enumerate(specList):
        specializationObj = {}
        specializationObj['id'] = idx
        specializationObj['name'] = key
        specializationArray.append(specializationObj)
    print(specializationArray)
    return jsonify({'specializations' : specializationArray})


@app.route("/results", methods=["GET", "POST"])
def results():

    return render_template('results.html')

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

        condition = dbConnection.insertNewUser(5, registerForm.email_address.data, 
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
    loginForm = forgotPwForm()
    if loginForm.errors != {}:
        for err_msg in loginForm.errors.values():
            flash(f'Error {err_msg}', category = 'danger')
    return render_template('forgotpw.html', form = loginForm)

@login_manager.user_loader
def load_user(user_id):
    df = dbConnection.getUserData()
    df = df.loc[df['userMail'] == user_id]
    user = User()
    user.create_user(df)
    return user
