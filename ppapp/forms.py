from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class PhoneForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditPhoneForm(PhoneForm):
	delete = BooleanField('Delete')

class ParamForm(FlaskForm):
	param = SelectField('Parameter', validators=[DataRequired()])
	value = StringField('Value', validators=[DataRequired()])
	submit = SubmitField('Submit')