
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

produtos_blueprint = Blueprint('produtos', __name__)

@produtos_blueprint.route("/produtos")
def produtos():
  return render_template("erro.html")
