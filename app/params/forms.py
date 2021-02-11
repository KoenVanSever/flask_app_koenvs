from flask_wtf import FlaskForm
from wtforms import MultipleFileField
from wtforms.validators import Regexp
# import email_validator


class UploadCsvForm(FlaskForm):
    files = MultipleFileField(label="File(s) to upload (only CSV allowed):")
    # validators=[Regexp(".*\.csv$")]
