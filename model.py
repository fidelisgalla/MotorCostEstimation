from wtforms import Form,FloatField,validators,SelectField

class InputFormMotor(Form):
    motorVoltage= SelectField(label='Motor Class Voltage (Volt)',default = 0, choices=['380 V','3300 V'],
                   validators=[validators.InputRequired()])
    motorCapacity = FloatField(label='capacity (kW)', default=0,
                   validators=[validators.InputRequired()])

class InputFormKabel(Form):
    cableVoltage = SelectField(label='Kabel Class Voltage (Voltage)', default=0, choices=['380 V', '3300 V'],
                             validators=[validators.InputRequired()])
    cableSize = SelectField(label='Cable Size (sqmm)', default=0, choices=['4x16 sqmm','4x25 sqmm','4x35 sqmm'],
                             validators=[validators.InputRequired()])


