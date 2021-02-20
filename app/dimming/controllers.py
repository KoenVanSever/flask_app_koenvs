from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app import db, login_required

# used in app/__init__.py
dimming = Blueprint('dimming', __name__, url_prefix='/dimming')


@dimming.route("/")
@login_required
def index():
    return render_template("dimming/index.html")
