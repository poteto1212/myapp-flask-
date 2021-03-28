from flask import Flask, request, render_template
import codecs
app = Flask(__name__)

@app.route("/")
def bbs():
    message = "Hello world"
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("bbs.html", message = message, lines = lines)

@app.route("/result", methods=["POST"])
def result():
    message = "This is paiza"
    article = request.form["article"]
    name = request.form["name"]
    file=codecs.open("articles.txt","a","utf-8")#articles.txtに対する書き込み設定 file変数に代入する
    file.write(article+","+name+"\n")#articleとnameをカンマで区切って入力
    file.close()
    return render_template("bbs_result.html", message = message, article = article, name = name)