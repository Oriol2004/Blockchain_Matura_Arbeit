from flask import Blueprint, render_template

#Blueprint wird erstellt um den Link zu URL herzustellen.

views = Blueprint("views",__name__)
#Basic route dann mach home!
@views.route("/")

def home():
    return render_template("home.html")