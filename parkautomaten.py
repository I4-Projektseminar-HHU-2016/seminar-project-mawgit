# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, flash, request, session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from database import db_session
from forms import LoginForm, EditPasswordForm, NewUserForm, EditUserForm, EditUserPasswordForm
from hash_passwords import make_hash
from sqlalchemy import asc
from sqlalchemy.sql import text,bindparam
from models import User
import config


app = Flask(__name__)
app.debug = True
app.config.from_object(config)


# Integration of Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@login_required
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # on POST check if the submitted form is valid
    if form.validate_on_submit():

        # get user from database
        user = User.query.filter_by(username=form.username.data).first()

        #check if the user exists and if he/she provided correct password
        #if user is not None and user.valid_password == form.password.data:
        if user is not None and user.valid_password(form.password.data):
            if login_user(user, remember=form.remember.data):
                session.permanent = not form.remember.data
                flash('Logged in successfully.')
                return redirect(request.args.get('next') or url_for('index'))
            else:
                flash('This account is disabled')
        else:
            flash('Wrong username and / or password')

    # on GET, just render the template with login form
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('index'))


@app.route("/index")
def func1():
    return render_template('/index.html')


@app.route("/automap")
def func2():
    #return render_template('/maps/park_staticmap.html')
    return redirect(url_for('static', filename='park_staticmap.html'))
    #return render_template(url_for('static', filename='park_staticmap.html'))
    #return redirect('park_staticmap.html') #The requested URL was not found on the server. Even if the file is in the root...
    #return app.send_static_file('/maps/park_staticmap.html')  #The requested URL was not found on the server. Even if the file is in the root...
    #return app.send_file('/maps/park_staticmap.html')  #AttributeError: 'Flask' object has no attribute 'send_file'


@app.route("/busmap")
def func3():
    return render_template('/maps/bus_staticmap.html')
    #return redirect(url_for('static', filename='bus_staticmap.html'))
    #return app.send_static_file('/maps/bus_staticmap.html')
    #return app.send_file('/maps/bus_staticmap.html')


@app.route("/heatmap")
def func4():
    return render_template('/maps/heatmap_parkautomaten.html')
    #return app.send_static_file('/maps/heatmaptestAI.html')
    #return app.send_file('/maps/heatmaptestAI.html')


if __name__ == "__main__":
    app.run()


