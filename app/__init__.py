from flask import Flask, Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import os

# -------------
# -- Init tasks
# -------------

app = Flask(__name__)
app.config.from_object("config")

#! define database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

#! define login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


from app.params.controllers import params
from app.dimming.controllers import dimming
from app.magnetics.controllers import magnetics
# from app.profile.controllers import profile as prof
app.register_blueprint(params)
app.register_blueprint(dimming)
app.register_blueprint(magnetics)
# app.register_blueprint(prof)
from app.params import models
from app.dimming import models

# --------------
# -- Login tasks
# --------------

from app.forms import LoginForm, RegisterForm
from app.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the that the form is submitted and validated
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("password and email ok")
            return redirect(url_for("index"))
        else:
            flash('Wrong email or password', 'error-message')
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        if form.password.data != form.repeat_password.data:
            return render_template("auth/register.html", form=form, message="Passwords don't match")
        else:
            # -- Using the generate_password_hash and check_password_hash includes hash salting automatically
            user = User(form.username.data, form.email.data,
                        generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
        return render_template("auth/register.html", form=form, message="User successfully made")
    return render_template("auth/register.html", form=form)


@app.route("/")
@login_required
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/<user_id>", methods=["GET"])
@login_required
def user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return render_template("auth/user_profile.html", user=user)
    else:
        return redirect(url_for("index"))
