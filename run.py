from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('quiz.html')


@app.route('/confirm', methods=['POST'])
def confirm():
   details = {}
   
 
   for input in request.form:
       if input == 'planet' or input == 'mercury' or input == 'venus' or input == 'name' or input == 'Mercury' or input == 'Saturn':
           details[input] = request.form[input]
   print(details)
   return render_template('confirm.html', details=details)
