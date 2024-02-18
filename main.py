from flask import Flask,render_template,request
app = Flask("name")



@app.route('/',methods = ['POST'])
def registr():
    userName = request.form["userName"]
    surname = request.form["surname"]
    login = request.form["login"]
    password = request.form["password"]
    return render_template('registrUser.html',userName=userName,surname=surname,
                           login=login,password=password)

if __name__ == "__main__":
    app.run(debug=True)