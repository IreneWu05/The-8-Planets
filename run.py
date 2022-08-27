from flask import Flask, render_template, request
app = Flask(__name__)

#import database for the planets
import sqlite3


#execute specific data for each planet
@app.route('/earth')
def earth():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 1")
    return render_template('earth.html', items=res.fetchall())

@app.route('/mercury')
def mercury():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 2")
    return render_template('mercury.html', items=res.fetchall())

@app.route('/venus')
def venus():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 3")
    return render_template('venus.html', items=res.fetchall())


@app.route('/mars')
def mars():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 4")
    return render_template('mars.html', items=res.fetchall())


@app.route('/jupiter')
def jupiter():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 5")
    return render_template('jupiter.html', items=res.fetchall())

@app.route('/saturn')
def saturn():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 6")
    return render_template('saturn.html', items=res.fetchall())

@app.route('/uranus')
def uranus():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 7")
    return render_template('uranus.html', items=res.fetchall())


@app.route('/neptune')
def neptune():
    con = sqlite3.connect('planetdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT distance, diameter, rotatetime, discoveredtime, daylength from planet WHERE id = 8")
    return render_template('neptune.html', items=res.fetchall())



@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/')
def index():
    return render_template('index.html')


#display quiz inputs in confirm.html
@app.route('/confirm', methods=['POST'])
def confirm():
   details = {}

   
   for input in request.form:
       if input == 'planet' or input == 'mercury' or input == 'venus' or input == 'name' or input == 'Mercury' or input == 'Saturn':
           details[input] = request.form[input]
   print(details)

   return render_template('confirm.html', details=details)







