# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, request, flash
from home.controller import ControllerAcounts

home = Blueprint('home', __name__, template_folder="templates",
                 static_folder="static", static_url_path="/home/static")

class Project(object):
    def __init__(self, *args):
        ...
    
    @home.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            name = request.form.get("inp_name")
            email = request.form.get("inp_email")

            """ Check if acount exists """
            user = ControllerAcounts().get_acount_existent(email)
            if user["status"] == 200 and name and email:

                """ Register new acount  """
                new = ControllerAcounts().insert_new_acount(name, email)
                if new["status"] == 200:
                    flash("User registred sucessfully")
                    return render_template("email.html", widget_class="is-primary")

                else:
                    flash(new["error"])
                    return render_template("email.html", widget_class="is-danger")

            else:
                flash("User exist, enter as new email")
                render_template("email.html", widget_class="is-danger")
            
        return render_template("email.html", widget_class="is-danger")

        
    