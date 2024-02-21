from flask import Flask,render_template,request
app = Flask("flaskapp")

@app.route("")
def registr():

    return render_template("registrUser.html")

@app.route("/user",metods=['POST'])
def user():
    userName = request.form["userName"]
    surname = request.form["surname"]
    login = request.form["login"]
    password = request.form["password"]
    return render_template("user.html",userName=userName,surname=surname,
                           login=login,password=password)

if __name__ == "__main__":
    app.run(debug=True)