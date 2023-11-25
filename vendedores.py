
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

vendedores_blueprint = Blueprint('vendedores', __name__)

@vendedores_blueprint.route("/vendedores")
def vendedores():
  return render_template("vendedores.html")
