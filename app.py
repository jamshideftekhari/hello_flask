from flask import Flask
from flask import render_template
from datetime import datetime
from Models.Die import Die 
from Models.Pizza.Menu import Menu

app = Flask(__name__)
@app.route("/") 
def home():
    d1=Die(0,"")
    d1.roll()
    fv = d1.GetFaceValue()
    return "hello flask. Dice result: " + str(fv) + " time: " + str(datetime.now())

@app.route("/DiceGame/") 
def hello_name():
    d1 = Die(0,"")
    d2 = Die(0,"")
    d1.roll()
    d2.roll()
    return render_template("DieGame.html", die1 = d1, die2 = d2)

@app.route("/Pizza_menu/") 
def pizza_menu():
    return render_template("pizzaMenu.html")
app.run()    