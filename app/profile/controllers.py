from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app import db
from app.mod_auth.models import User
# used in app/__init__.py
profile = Blueprint('prof', __name__, url_prefix='/prof')
