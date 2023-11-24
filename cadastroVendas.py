
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

cadastroVendas_blueprint = Blueprint('cadastroVendas', __name__)

@cadastroVendas_blueprint.route("/cadastroVendas")
def cadastroVendas():
  return render_template("cadastroVendas.html")


@cadastroVendas_blueprint.route("/cadastroVendas")
def listar_clientes():
    bd = db.SQLiteConnection('estoque.db') 
    bd.connect()
    clientes = bd.execute_query("SELECT * FROM clientes;")
    return render_template("cadastroVendas.html", dados=clientes)

@cadastroVendas_blueprint.route("/produtos")
def listar_produtos():
    bd = db.SQLiteConnection('estoque.db') 
    bd.connect()
    produtos = bd.execute_query("SELECT * FROM produtos;")
    return render_template("cadastroVendas.html", dados=produtos)


@cadastroVendas_blueprint.route("/clientes/adicionar", methods=["POST"])
def adicionar_cliente():
    if request.method == "POST":
        id_cliente = request.form.get('nome_cliente')
        id_produto = request.form.get('produto')
        quantidade = request.form.get('quantidade') 

        bd = db.SQLiteConnection('estoque.db')
        bd.connect()
        query = "INSERT INTO vendas (id_cliente, id_produto, quantidade) VALUES (?, ?, ?);"
        bd.execute_query(query, (id_cliente, id_produto, quantidade))

        return redirect("/clientes")
