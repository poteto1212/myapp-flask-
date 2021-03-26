from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello_world():
    name='Flask'
    return render_template("index.html",name_value=name)

@app.route("/about")
def about():
    return render_template("index.html")
    