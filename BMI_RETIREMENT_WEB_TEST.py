import BMI_DB_Stub, BMI_DB_Stub2, Retirement_DB_Stub, Retirement_DB_Stub2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/BMI')
def retrieveBMI():
    return render_template('Results.html', entries=BMI_DB_Stub.retrieveEntry())

@app.route('/BMI/<height_feet>/<height_inches>/<weight>')
def bmi(height_feet, height_inches, weight):
    BMI_DB_Stub2.canAddEntry(height_feet, height_inches, weight)
    return 'Request Accepted'

@app.route('/RETIREMENT')
def retrieveRETIREMENT():
    return render_template('Results.html', entries=Retirement_DB_Stub.retrieveEntry())

@app.route('/RETIREMENT/<age>/<salary>/<percentage>/<goal>')
def retirement(age, salary, percentage, goal):
    Retirement_DB_Stub2.canAddEntry(age, salary, percentage, goal)
    return 'Request Accepted'

if __name__=="__main__":
    app.run()