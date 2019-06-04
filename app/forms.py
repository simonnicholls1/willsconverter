from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class ConverterForm(FlaskForm):
    types = RadioField('Type', choices=[('Kgs', 'Kgs'), ('Lbs', 'Lbs')])
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Convert')
