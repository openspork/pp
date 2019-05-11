from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from ppapp.models import *

class PhoneForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditPhoneForm(PhoneForm):
	delete = BooleanField('Delete')

param_form_choices = []
for choice in BaseParam.select().order_by(BaseParam.name):
    choice_string = '%s - Default: %s' % (choice.name[1:], choice.default_value[:32])
    param_form_choices.append((choice.id, choice_string))

class ParamForm(FlaskForm):
	param = SelectField('Parameter', choices = param_form_choices, validators=[DataRequired()], coerce = int)
	value = StringField('Value', validators=[DataRequired()])
	note = StringField('Note')
	submit = SubmitField('Submit')