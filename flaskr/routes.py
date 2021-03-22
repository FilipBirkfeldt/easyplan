from flaskr import app
from flask import render_template, url_for

@app.route("/")
def index():
    return render_template("index.html")

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