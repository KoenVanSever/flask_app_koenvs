from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for, send_file
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
    params_list = Params.query.order_by(Params.csv_name.asc())
    upload_form = UploadCsvForm()
    if upload_form.validate_on_submit():
        uploaded = upload_form.files.data
        for file in uploaded:
            if Params.query.filter_by(csv_name=file.filename).first():
                print("File '%s': name already taken" % file.filename)
                flash("File '%s': name already taken" % file.filename, category="warning")
                continue
            path = Path("app", "temporary", file.filename)
            temp = file.save(path)  # TODO: (1)
            try:
                param = Params.upload_file(path)
                param.light_family = upload_form.category.data
                db.session.add(param)
                flash("File '%s': added to database" % param.csv_name, category="success")
            except AttributeError:
                print("File '%s': invalid data type" % file.filename)
                flash("File '%s': invalid data type" % file.filename, category="error")
            finally:
                os.remove(path)
        db.session.commit()
        params_list = Params.query.order_by(Params.csv_name.asc())
    return render_template("params/index.html", params=params_list, upload_form=upload_form)


@params.route("/<param_id>", methods=["GET", "POST"])
@login_required
def detail(param_id):
    param = Params.query.filter_by(id=param_id).first()
    # TODO: implement next/prev param
    order_id = [x.id for x in Params.query.order_by(Params.csv_name.asc())]
    pos = order_id.index(int(param_id))
    try:
        prev_id = order_id[pos - 1]
        next_id = order_id[(pos + 1) if pos < (len(order_id) - 1) else 0]
    except IndexError:
        flash("Something went wrong determining next parameter in sequence", "error")
    if request.method == "POST":
        if param.query.filter_by(csv_name=request.form["csv_name"]).first():
            param.update_with_dict(request.form)
            flash("File '{}' updated in database".format(request.form['csv_name']), category="info")
        else:
            temp = Params()
            temp.update_with_dict(request.form)
            db.session.add(temp)
            flash("File '{}' added to database".format(request.form['csv_name']), category="success")
            param = temp
        db.session.commit()
    return render_template("params/detail.html", param=param, id_prev_next=[prev_id, next_id])


@params.route("delete/<param_id>")
@login_required
def delete(param_id):
    param = Params.query.filter_by(id=param_id).first()
    db.session.delete(param)
    db.session.commit()
    flash("File '%s' delete from database" % param.csv_name, category="info")
    return redirect(url_for("params.index"))


@params.route("export/<param_id>")
@login_required
def export(param_id):
    param = Params.query.filter_by(id=param_id).first()
    param.export_csv()
    return send_file(Path("temporary", param.csv_name), as_attachment=True, mimetype="text/csv", attachment_filename=param.csv_name)
