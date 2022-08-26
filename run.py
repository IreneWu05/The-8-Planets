from flask import Flask, render_template, request
app = Flask(__name__)

#import database for the planets
import sqlite3


#execute specific data
@app.route('/earth')
def earth():
    con = sqlite3.connect('planetdata.db')
    db = con.cursor()
    res = db.execute("SELECT distance from planet WHERE id = 1")
    return render_template('earth.html', distances=res.fetchall())





@app.route('/')
def quiz():
    return render_template('quiz.html')





#display quiz inputs in confirm.html
@app.route('/confirm', methods=['POST'])
def confirm():
   details = {}

   
   for input in request.form:
       if input == 'planet' or input == 'mercury' or input == 'venus' or input == 'name' or input == 'Mercury' or input == 'Saturn':
           details[input] = request.form[input]
   print(details)

   return render_template('confirm.html', details=details)







