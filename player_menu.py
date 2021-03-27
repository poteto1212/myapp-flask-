from flask import Flask, render_template
app=Flask(__name__)

player="勇者"

#メニュー
@app.route("/")
def menu():
    return render_template("menu.html",player=player)
    
    
#あるく
@app.route("/walk")
def walk():
    message=player+"は荒野を歩いていた"
    return render_template("action.html",player=player,message=message)

@app.route("/attack")
def attack():
    message=player+"はモンスターと戦った"
    return render_template("action.html",player=player,message=message)
    
