from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def show():
    message="hello world"
    return render_template("form.html",message=message)

@app.route("/result", methods=["GET","POST"])
def result():
    message = "This is paiza"
    if request.method=="POST":#formタグがpostメソッドを指定している場合の処理
        article = request.form["article"]#HTML上のformタグのforからデータを受け取っている。
        name = request.form["name"]
    else:#formタグがgetメソッドを指定している場合の処理
        article=request.args.get("article")
        name=request.args.get("name")
        #getメソッド→検索フォームによく使う
        #postメソッド→パスワード等の送信によく使う
    
    return render_template("form.html", message = message, article = article, name = name)