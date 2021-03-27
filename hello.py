from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello_world():
    name='Flask'
    players=['勇者','戦士','魔法使い']
    return render_template("index.html",name_value=name,players=players)

@app.route("/about")
def about():
    return render_template("index.html")
    