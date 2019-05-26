from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    BooleanField,
    SubmitField,
    SelectField,
    SelectMultipleField,
    TextAreaField,
)
from wtforms.validators import DataRequired, MacAddress, NumberRange

# Careful, ppapp.models will clobber wtforms' BooleanField!
from ppapp.models import BaseParam, AvailParam, Group, GroupType


def get_form_choices(query, Model):
    form_choices = []
    for choice in query:
        if Model == Group:
            choice_string = "%s: %s" % (choice.type.name, choice.name)
        elif Model == BaseParam:
            choice_string = "%s - Default: %s" % (
                choice.name[1:],
                choice.default_value[:24],
            )
        elif Model == AvailParam:
            choice_string = "%s - Value: %s" % (
                choice.base_param.name[1:],
                choice.value[:16],
            )
        else:
            choice_string = choice.name

        form_choices.append((choice.id, choice_string))
    return form_choices


class NameNoteSubmitForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    note = StringField("Note")
    submit = SubmitField("Submit")


class PhoneForm(NameNoteSubmitForm):
    mac_address = StringField("MAC Address", validators=[DataRequired(), MacAddress()])


class NewPhoneForm(PhoneForm):
    pass


class DeleteForm(FlaskForm):
    delete = BooleanField("Delete")


class AddRemoveParamForm(FlaskForm):
    # Params
    avail_params = SelectMultipleField(
        "Available Parameters - Select to Apply", coerce=int
    )
    active_params = SelectMultipleField(
        "Active Parameters - Select to Remove", coerce=int
    )


class AddRemoveGroupForm(FlaskForm):
    # Groups
    avail_groups = SelectMultipleField("Available groups - Select to Apply", coerce=int)
    active_groups = SelectMultipleField("Active groups - Select to Remove", coerce=int)


class EditPhoneForm(PhoneForm, AddRemoveParamForm, AddRemoveGroupForm, DeleteForm):
    reissue_cert = BooleanField()


class ParamForm(FlaskForm):
    note = StringField("Note")
    submit = SubmitField("Submit")
    value = StringField("Value", validators=[DataRequired()])
    pass


class NewParamForm(ParamForm):

    param = SelectField(
        "Parameter",
        choices=get_form_choices(
            BaseParam.select().order_by(BaseParam.name), BaseParam
        ),
        validators=[DataRequired()],
        coerce=int,
    )


class EditParamForm(ParamForm, DeleteForm):
    pass


class GroupForm(NameNoteSubmitForm):
    type = SelectField("Type", coerce=int)
    pass


class NewGroupTypeForm(NameNoteSubmitForm, DeleteForm):
    precedence = IntegerField(validators=[NumberRange(min = 0, max = 100)])


class EditGroupTypeForm(NewGroupTypeForm):
    pass


class NewGroupForm(GroupForm):
    pass


class CertAuthorityForm(NameNoteSubmitForm, FlaskForm):
    cert = TextAreaField("Cert", validators=[DataRequired()])
    private_key = TextAreaField("Private Key", validators=[DataRequired()])
    cert_revocation_list = TextAreaField("CRL (Blank for New")


class NewCertAuthorityForm(CertAuthorityForm):
    pass


class EditCertAuthorityForm(CertAuthorityForm, DeleteForm):
    pass


class SelectCertAuthorityForm(FlaskForm):
    cert_authority = SelectField("Available CAs", coerce=int, default=0)


class EditGroupForm(GroupForm, DeleteForm, AddRemoveParamForm, SelectCertAuthorityForm):
    avail_parents = SelectMultipleField("Available parents", coerce=int)
    active_parents = SelectMultipleField("Active parents", coerce=int)
    avail_children = SelectMultipleField("Available children", coerce=int)
    active_children = SelectMultipleField("Active children", coerce=int)
