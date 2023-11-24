
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

produtos_blueprint = Blueprint('produtos', __name__)

"""
@produtos_blueprint.route("/produtos")
def produtos():
  return render_template("produtos.html", produtos=[])

"""
@produtos_blueprint.route("/produtos")
def produtos():
    try:
        produtos = db.produtos()  # Substitua esta linha conforme necessário
        return render_template("produtos.html", produtos=produtos)
    except Exception as e:
        return f"Erro ao carregar produtos: {str(e)}"

