from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('quiz.html')


@app.route('/confirm', methods=['POST'])
def confirm():
   details = {}
   items = {}
   
 
   for input in request.form:
       if input == 'planet' or input == 'mercury':
           details[input] = request.form[input]
       elif request.form[input] and request.form[input] != '0':
           items[input] = request.form[input]
   print(details)
   return render_template('confirm.html', details=details, items=items)
