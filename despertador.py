from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def inicial():
  return render_template("despertador.html")

@app.route("/despertar")
def despertar():
  return render_template("acordar.html") 
app.run(debug=True,host='0.0.0.0')                       