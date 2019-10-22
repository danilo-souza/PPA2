import BMI, Retirement
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/BMI')
def retrieveBMI():
    return render_template('Results.html', entries=BMI.retrieveEntry())

@app.route('/BMI/<height_feet>/<height_inches>/<weight>')
def bmi(height_feet, height_inches, weight):
    BMI.BMI(height_feet, height_inches, weight)
    return 'Request Accepted'

@app.route('/RETIREMENT')
def retrieveRETIREMENT():
    return render_template('Results.html', entries=Retirement.retrieveEntry())

@app.route('/RETIREMENT/<age>/<salary>/<percentage>/<goal>')
def retirement(age, salary, percentage, goal):
    Retirement.retirement(age, salary, percentage, goal)
    return 'Request Accepted'

if __name__=="__main__":
    app.run()