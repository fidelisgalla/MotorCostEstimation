#this file is used for testing the compute file

from compute import CalculationMotorPrice


priceMotor = CalculationMotorPrice()

computeMotor = priceMotor.computeMotorMediumVoltage(500)
print(computeMotor)