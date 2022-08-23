from flask import Flask,render_template,request
from model import InputFormMotor, InputFormKabel
from wtforms import Form, FloatField, validators
from compute import CalculationMotorPrice
import sys

app = Flask(__name__)

@app.route('/motor',methods=['GET','POST'])
def indexMotor():
    form = InputFormMotor(request.form)
    if request.method == 'POST' and form.validate():
        priceMotor = CalculationMotorPrice()
        result = priceMotor.computeMotorMediumVoltage(form.motorVoltage.data,form.motorCapacity.data)
    else:
        result = None

    return render_template("view.html",form = form, result = result)


if __name__ =='__main__':
    app.run(debug=True)
