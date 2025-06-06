from flask import render_template
from utils.routing import route

@route("/")
def home():
    return render_template("index.html")