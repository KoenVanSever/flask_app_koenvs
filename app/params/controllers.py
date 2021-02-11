from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for
from app.params.forms import UploadCsvForm
from app import db, login_required
from app.params.models import *
from app import app  # needed?
from pathlib import Path
import os

# TODO: (1) write FileStorage/stream backend in model

params = Blueprint('params', __name__, url_prefix='/params')


@params.route("/", methods=["GET", "POST"])
@login_required
def index():
    params_list = Params.query.all()
    upload_form = UploadCsvForm()
    if upload_form.validate_on_submit():
        uploaded = upload_form.files.data
        for file in uploaded:
            if Params.query.filter_by(csv_name=file.filename).first():
                print("File '%s': name already taken" % file.filename)
                flash("File '%s': name already taken" % file.filename, category="warning")
                continue
            path = Path("temporary", file.filename)
            temp = file.save(path)  # TODO: (1)
            try:
                param = Params.upload_file(path)
                db.session.add(param)
            except AttributeError:
                print("File '%s': invalid data type" % file.filename)
                flash("File '%s': invalid data type" % file.filename, category="error")
            finally:
                os.remove(path)
        db.session.commit()
        params_list = Params.query.all()
    return render_template("params/index.html", params=params_list, upload_form=upload_form)


@params.route("/<param_id>", methods=["GET", "POST"])
@login_required
def detail(param_id):
    param = Params.query.filter_by(id=param_id).first()
    if request.method == "POST":
        if param.query.filter_by(csv_name=request.form["csv_name"]).first():
            param.update_with_dict(request.form)
            flash("File '{}' updated in database".format(request.form['csv_name']), category="info")
        else:
            temp = Params()
            temp.update_with_dict(request.form)
            db.session.add(temp)
            flash("File '{}' added to database".format(request.form['csv_name']), category="info")
            param = temp
        db.session.commit()
    return render_template("params/detail.html", param=param)
