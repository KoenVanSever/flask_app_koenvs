from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app import db, login_required
import pandas as pd
from .forms import UploadCsvForm
from .models import Dimming
from werkzeug.utils import secure_filename
from pathlib import Path
from app import app
from flask import json
from .support_functions import *
import plotly.express as px
import plotly.io as po
import os

# used in app/__init__.py
dimming = Blueprint('dimming', __name__, url_prefix='/dimming')


@dimming.route("/", methods=["GET", "POST"])
@login_required
def index():
    # -- Form creation
    upload_form = UploadCsvForm()

    # -- process form
    if upload_form.validate_on_submit():
        uploaded_info = upload_form.data
        uploaded_file = upload_form.file.data

        basename = uploaded_file.filename
        target_path = Path(app.config["UPLOAD_FOLDER"], basename).resolve()
        name = secure_filename(uploaded_info.pop("name")) if uploaded_info["name"] != "" else basename.split(".")[0]
        color = uploaded_info.pop("color_type", None)

        if Dimming.query.filter_by(name=name).first():
            print("File '%s': name already taken" % name)
            flash("File '%s': name already taken" % name, category="warning")
        else:
            uploaded_file.save(target_path)
            dim = Dimming(filename=str(target_path), name=name, color_type=color)
            print("File '%s': added to database" % name)
            flash("File '%s': added to database" % name, category="success")
            db.session.add(dim)
            db.session.commit()

    # -- generate context
    dimming_list = Dimming.query.all()
    plotly_json = json.dumps([])
    # {"x": [2800, 6600], "y":[0, 100], "type": "scatter"}

    # -- formulate response
    return render_template("dimming/index.html", upload_form=upload_form, dimming_list=dimming_list, plotly_json=json.loads(plotly_json))


@dimming.route("/get_curve/<name>")
@login_required
def get_curve(name):
    target = Dimming.query.filter_by(name=name).first()
    df = pd.read_csv(target.filename)
    print(target, target.color_type)
    lower_data, upper_data = retrieve_limits(target.color_type)
    name_data = {"x": list(df.input), "y": list(df.output), "type": "scatter", "name": target.name}
    data = [name_data, lower_data, upper_data]
    return json.dumps(data)


@dimming.route("/delete_file/<file>", methods=["POST"])
@login_required
def get_list(file):
    print(file)
    db_entry = Dimming.query.filter_by(name=file).first()
    os.remove(db_entry.filename)
    db.session.delete(db_entry)
    db.session.commit()
    return redirect(url_for('dimming.index'))
