
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

atividades_blueprint = Blueprint('atividades', __name__)

@atividades_blueprint.route("/atividades")
def atividades():
  return render_template("dashboard.html")
