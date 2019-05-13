from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
# Careful, ppapp.models will clobber wtforms' BooleanField!
from ppapp.models import BaseParam, AvailParam, Group, GroupType

def get_form_choices(query, Model):
    form_choices = []
    for choice in query:
        if Model == Group:
            choice_string = '%s: %s' % (choice.type.name, choice.name)
        if Model == BaseParam:
            choice_string = '%s - Default: %s' % (choice.name[1:], choice.default_value[:32])
        if Model == AvailParam:
            choice_string = '%s - Value: %s' % (choice.base_param.name[1:], choice.value)
        if Model == GroupType:
            choice_string = choice.name
        form_choices.append((choice.id, choice_string))
    return form_choices

class PhoneForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired()])
    note = StringField('Note')
    submit = SubmitField('Submit')

class NewPhoneForm(PhoneForm):
    pass

class DeleteForm(FlaskForm):
    delete = BooleanField('Delete')

class AddRemoveParamForm(DeleteForm):
    # Params
    avail_params = SelectMultipleField('Available Parameters - Select to Apply', coerce = int)
    active_params = SelectMultipleField('Active Parameters - Select to Remove', coerce = int)
    # Groups
    avail_groups = SelectMultipleField('Available groups - Select to Apply', coerce = int)
    active_groups = SelectMultipleField('Active groups - Select to Remove', coerce = int)

class EditPhoneForm(PhoneForm, AddRemoveParamForm):
    pass

class ParamForm(FlaskForm):
    value = StringField('Value', validators=[DataRequired()])
    note = StringField('Note')
    submit = SubmitField('Submit')

class NewParamForm(ParamForm):
    param = SelectField('Parameter', choices = get_form_choices(BaseParam.select().order_by(BaseParam.name), BaseParam), validators=[DataRequired()], coerce = int)

class EditParamForm(ParamForm, DeleteForm):
    pass

class GroupForm(FlaskForm):
    type = SelectField('Type', choices = get_form_choices(GroupType.select().order_by(GroupType.name), GroupType), coerce = int)
    name = StringField('Name')
    note = StringField('Note')
    submit = SubmitField('Submit')

class NewGroupForm(GroupForm):
    pass

# class EditGroupForm(GroupForm, DeleteForm, EditForm):
#     pass
