from flask import Flask, render_template, request
app = Flask(__name__)

#import database for the planets
import sqlite3
conn = sqlite3.connect('planetdata.db')

#execute specific data
cursor = conn.execute("SELECT distance from planet WHERE id = 1")
for row in cursor:
    print("earth distance = ", row[0])
def earth():
    return render_template('earth.html')
conn.close()



@app.route('/')
def index():
    return render_template('quiz.html')


@app.route('/earth')
def earth():
    return render_template('earth.html')



#display quiz inputs in confirm.html
@app.route('/confirm', methods=['POST'])
def confirm():
   details = {}

   
   for input in request.form:
       if input == 'planet' or input == 'mercury' or input == 'venus' or input == 'name' or input == 'Mercury' or input == 'Saturn':
           details[input] = request.form[input]
   print(details)

   return render_template('confirm.html', details=details)







