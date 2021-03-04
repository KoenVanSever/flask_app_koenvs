from flask_wtf import FlaskForm
from wtforms import FileField, StringField, RadioField
from wtforms.validators import Regexp
# import email_validator


class UploadCsvForm(FlaskForm):
    file = FileField(label="File:")
    name = StringField(label="Name:")
    color_type = RadioField(label="Color:", choices=["color", "white"])
