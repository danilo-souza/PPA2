import BMI_DB_Fake, Retirement_DB_Fake
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/BMI')
def retrieveBMI():
    return render_template('Results.html', entries=BMI_DB_Fake.retrieveEntry())

@app.route('/BMI/<height_feet>/<height_inches>/<weight>')
def bmi(height_feet, height_inches, weight):
    BMI_DB_Fake.canAddEntry(height_feet, height_inches, weight)
    return 'Request Accepted'

@app.route('/RETIREMENT')
def retrieveRETIREMENT():
    return render_template('Results.html', entries=Retirement_DB_Fake.retrieveEntry())

@app.route('/RETIREMENT/<age>/<salary>/<percentage>/<goal>')
def retirement(age, salary, percentage, goal):
    Retirement_DB_Fake.canAddEntry(age, salary, percentage, goal)
    return 'Request Accepted'

if __name__=="__main__":
    app.run()