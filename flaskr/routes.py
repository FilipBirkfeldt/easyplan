from flaskr import app
from flask import render_template, url_for, redirect, flash, request
from checkPoints_graduation.calculatePoints import getAllPointsDict
from flaskr.forms import Registrator, specChoices, programChoices
#from flaskr.forms import courseField
@app.route("/", methods =['GET', 'POST'])
def index():
   # cursor = mysql.connection.cursor()
   # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    data = {}   
    if request.method == 'POST':
        fullname = request.form.getlist('field[]')
        data = getAllPointsDict('M', 'Mekatronik', fullname)
        return render_template('index.html', data = data)
        #send_data för att ladda ner excel filer t.ex.
    return render_template('index.html', data=data)

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
def registration_page():
    loginForm = Registrator()
    if loginForm.validate_on_submit():
        test = 'Submit funka'
    if loginForm.errors != {}:
        for err_msg in loginForm.errors.values():
            flash(f'There was an error with creating a user {err_msg}', category = 'danger')
            #return redirect(url_for('registration_page'))

    return render_template('register.html', form = loginForm)


if __name__ == "__main__":
    app.run(debug=True)