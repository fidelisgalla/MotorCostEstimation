########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from flask import Flask,render_template,request
from model import InputFormMotor, InputFormKabel
from wtforms import Form, FloatField, validators
from compute import CalculationMotorPrice

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

#pada bagian ini, kita dapat memasukkan bagian dari kode yang akan digunakan
@main.route('/motor',methods=['GET','POST']) # profile page that return 'profile'
@login_required
def index_motor():
    form = InputFormMotor(request.form)
    if request.method == 'POST' and form.validate():
        priceMotor = CalculationMotorPrice()
        result = priceMotor.computeMotorMediumVoltage(form.motorVoltage.data, form.motorCapacity.data)
    else:
        result = None

    return render_template("view.html",form=form,result = result)

app = create_app() # we initialize our flask app using the __init__.py function

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode