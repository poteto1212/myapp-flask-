from flask import Flask, request, render_template
app = Flask(__name__)

players = ["勇者", "戦士", "魔法使い", "忍者"]

@app.route("/")#テンプレートのgetメソッドに直接表示
def show():
    message = "あらたなモンスターがあらわれた！"
    return render_template("battle.html", message = message, players = players)

@app.route("/result", methods=["POST"])#テンプレートのPOSTメソッドからの入力処理
def result():
    name = request.form["name"]
    message = name + "はモンスターと戦った！"
    return render_template("battle.html", message = message, players = players)
