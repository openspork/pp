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
from wtforms.validators import DataRequired, MacAddress, NumberRange, URL

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


class AddRemoveParentForm(FlaskForm):
    avail_parents = SelectMultipleField(
        "Available parent groups - Select to Apply", coerce=int
    )
    active_parents = SelectMultipleField(
        "Active parent groups - Select to Remove", coerce=int
    )


class AddRemoveChildForm(FlaskForm):
    avail_children = SelectMultipleField(
        "Available child groups - Select to Apply", coerce=int
    )
    active_children = SelectMultipleField(
        "Active child groups - Select to Remove", coerce=int
    )


class PhoneForm(NameNoteSubmitForm):
    mac_address = StringField("MAC Address", validators=[DataRequired(), MacAddress()])


class NewPhoneForm(PhoneForm, AddRemoveParamForm, AddRemoveParentForm):
    pass


class EditPhoneForm(PhoneForm, AddRemoveParamForm, AddRemoveParentForm, DeleteForm):
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
    precedence = IntegerField(validators=[NumberRange(min=0, max=100)])


class EditGroupTypeForm(NewGroupTypeForm):
    pass


class CertAuthorityForm(NameNoteSubmitForm, FlaskForm):
    cert = TextAreaField("Cert", validators=[DataRequired()])
    private_key = TextAreaField("Private Key", validators=[DataRequired()])
    cert_revocation_list = TextAreaField("CRL (Leave blank to generate)")


class NewCertAuthorityForm(CertAuthorityForm):
    country_name = StringField(
        "Two Character Country Code", validators=[DataRequired()]
    )
    state_or_province_name = StringField(
        "State or Province Name", validators=[DataRequired()]
    )
    locality_name = StringField("Locality Name", validators=[DataRequired()])
    organization_name = StringField("Organization Name", validators=[DataRequired()])
    cert_revocation_list_uri = StringField(
        "CRL URI", validators=[DataRequired(), URL()]
    )


class EditCertAuthorityForm(CertAuthorityForm, DeleteForm):
    pass


class SelectCertAuthorityForm(FlaskForm):
    cert_authority = SelectField("Available CAs", coerce=int, default=0)


class NewGroupForm(
    GroupForm, AddRemoveParentForm, AddRemoveParamForm, SelectCertAuthorityForm
):
    pass


class EditGroupForm(
    GroupForm,
    DeleteForm,
    AddRemoveChildForm,
    AddRemoveParentForm,
    AddRemoveParamForm,
    SelectCertAuthorityForm,
):
    pass
