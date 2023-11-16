
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

permissoes_blueprint = Blueprint('permissoes', __name__)

@permissoes_blueprint.route("/permissoes")
def permissoes():
  return render_template("erro.html")
