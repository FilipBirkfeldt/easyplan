from flaskr import app
from flask import render_template, url_for, redirect, flash, request
from checkPoints_graduation.calculatePoints import getAllPointsDict
#from flaskr.forms import courseField
@app.route("/", methods =['GET', 'POST'])
def index():
   # cursor = mysql.connection.cursor()
   # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    data = {}   
    if request.method == 'POST':
        fullname = request.form.getlist('field[]')
        data = getAllPointsDict('M', 'Mekatronik', fullname)

        #for value in fullname:  
         #   message += value
            #cur.execute("INSERT INTO fullnames (full_name) VALUES (%s)",[value])
            #mysql.connection.commit()       
        #cur.close()
        #message = fullname[0]
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



if __name__ == "__main__":
    app.run(debug=True)