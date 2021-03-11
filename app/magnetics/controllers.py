from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app import db, login_required, app
import pandas as pd
from pathlib import Path
from .forms import ConfigurationForm
from flask import json
from .support_functions import *

# used in app/__init__.py
magnetics = Blueprint('magnetics', __name__, url_prefix='/magnetics')

# -- factors dataframes
PERM_DC = pd.read_csv(Path(app.config["STATIC_FOLDER"], "info", "perm_dc.csv"))
CORE_LOSS = pd.read_csv(Path(app.config["STATIC_FOLDER"], "info", "core_loss.csv"))
NORM_MAGN = pd.read_csv(Path(app.config["STATIC_FOLDER"], "info", "normal_magn.csv"))
PERM_FREQ = pd.read_csv(Path(app.config["STATIC_FOLDER"], "info", "perm_freq.csv"))
PERM_TEMP = pd.read_csv(Path(app.config["STATIC_FOLDER"], "info", "perm_temp.csv"))
INFO_DICT = {"perm_dc": PERM_DC, "core_loss": CORE_LOSS, "norm_magn": NORM_MAGN, "perm_freq": PERM_FREQ, "perm_temp": PERM_TEMP}
MATERIAL_LIST = list(zip(["_".join(x.split(" ")) for x in PERM_DC.material.unique()], PERM_DC.material.unique()))
MATERIAL_SEARCH = dict(MATERIAL_LIST)
MATERIAL_SEARCH_INVERSE = dict(list(zip(PERM_DC.material.unique(), ["_".join(x.split(" ")) for x in PERM_DC.material.unique()])))


@magnetics.route("/")
@login_required
def index():
    form = ConfigurationForm()
    form.material.choices = MATERIAL_LIST
    return render_template("magnetics/index.html", form=form)


@magnetics.route("/set_mat/<mat>")
@login_required
def set_mat(mat):
    material = MATERIAL_SEARCH[mat]
    available_options = list(PERM_DC[PERM_DC.material == material].perm.unique())
    return json.dumps(list(map(str, available_options)))


@magnetics.route("/get_factors/<mat>/<perm>")
@login_required
def get_factors(mat, perm):
    factors_dict = dict()
    mat = MATERIAL_SEARCH[mat]
    factors_dict = get_specific_factors(mat, perm, ["a", "b", "c"], factors_dict, PERM_DC, "perm_dc")
    factors_dict = get_specific_factors(mat, perm, ["a", "b", "c"], factors_dict, CORE_LOSS, "core_loss")
    factors_dict = get_specific_factors(mat, perm, ["a", "b", "c", "d", "e", "x"], factors_dict, NORM_MAGN, "norm_magn")
    factors_dict = get_specific_factors(mat, perm, ["a", "b", "c", "d", "e"], factors_dict, PERM_FREQ, "perm_freq")
    factors_dict = get_specific_factors(mat, perm, ["a", "b", "c", "d", "e"], factors_dict, PERM_TEMP, "perm_temp")
    return json.dumps(factors_dict)
