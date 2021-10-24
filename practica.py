from flask import Flask, render_template

app = Flask(__name__)





@app.route("/template2.html")

def sanmiguel():

    return render_template("template2.html")

@app.route("/index.html")

def inicio2():

    return render_template("index.html")


@app.route("/")

def inicio():

    return render_template("index.html")


@app.route("/mayor.html")

def mayor():

    return render_template("mayor.html")
   



@app.route("/enlaces.html")

def Enlaces():

    return render_template("enlaces.html")


   


app.run(debug=True)