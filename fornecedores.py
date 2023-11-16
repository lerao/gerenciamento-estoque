
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

fornecedores_blueprint = Blueprint('fornecedores', __name__)

@fornecedores_blueprint.route("/fornecedores")
def fornecedores():
  return render_template("erro.html")
