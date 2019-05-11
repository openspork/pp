from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
# Careful, models will clobber wtforms' BooleanField!
from ppapp.models import BaseParam, AvailParam

class PhoneForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

def get_avail_param_form_choices(params):
    print(params)
    param_form_choices = []
    for choice in params:
        choice_string = '%s - Value: %s' % (choice.base_param.name[1:], choice.value)
        param_form_choices.append((choice.id, choice_string))
    return param_form_choices

def get_generic_param_form_choices(Param):
    param_form_choices = []
    if ( Param is BaseParam ):
        for choice in BaseParam.select().order_by(BaseParam.name):
            choice_string = '%s - Default: %s' % (choice.name[1:], choice.default_value[:32])
            param_form_choices.append((choice.id, choice_string))
    elif ( Param is AvailParam ):
        params = AvailParam.select().order_by(AvailParam.base_param.name)
        param_form_choices = get_generic_param_form_choices(params)
            
    return param_form_choices

class EditPhoneForm(PhoneForm):
    delete = BooleanField('Delete')
    avail_params = SelectMultipleField('Available Parameters - Select to Apply', choices = get_generic_param_form_choices(AvailParam), coerce = int)
    active_params = SelectMultipleField('Applied Paramters - Select to Remove', coerce = int)

class ParamForm(FlaskForm):
    param = SelectField('Parameter', choices = get_generic_param_form_choices(BaseParam), validators=[DataRequired()], coerce = int)
    value = StringField('Value', validators=[DataRequired()])
    note = StringField('Note')
    submit = SubmitField('Submit')