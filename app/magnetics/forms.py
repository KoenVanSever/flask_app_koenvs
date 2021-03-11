from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, IntegerField, RadioField
import pandas as pd
from pathlib import Path
from app import app


class ConfigurationForm(FlaskForm):
    material = SelectField(label="Material Selection:", choices=list())
    permeability = SelectField(label="Initial Permeability:", choices=list())
    dc_bias = DecimalField(label="Max Idc bias (A):")
    num_turns = IntegerField(label="Number of turns:")
    path_length = DecimalField(label="Path length (cm):")
    oersted = RadioField(label="Unit:", choices=["Oe", "AT/cm"])
    oersted_plot = IntegerField(label="Oersted for plot:")
