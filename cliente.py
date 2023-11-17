
from flask import Flask, render_template, request, redirect, Blueprint,jsonify;
import database as db;

clientes_blueprint = Blueprint('clientes', __name__)

@clientes_blueprint.route("/clientes")
def listar_clientes():
    bd = db.SQLiteConnection('estoque.db')
    bd.connect()
    clientes = bd.execute_query("SELECT * FROM clientes;")
    #return jsonify(clientes)
    return render_template("clientes.html", dados=clientes)

@clientes_blueprint.route("/clientes/adicionar", methods=["POST"])
def adicionar_cliente():
    if request.method == "POST":
        nome = request.form.get('nome')
        documento = request.form.get('documento')
        endereco = request.form.get('endereco') 
        telefone = request.form.get('telefone')
        data_nascimento = request.form.get('data_nascimento')

        bd = db.SQLiteConnection('estoque.db')
        bd.connect()
        query = "INSERT INTO clientes (nome, documento, endereco, telefone, data_nascimento) VALUES (?, ?, ?);"
        bd.execute_query(query, (nome, documento, endereco, telefone, data_nascimento))

        return redirect("/clientes")

@clientes_blueprint.route("/clientes/editar/<int:cliente_id>", methods=["GET", "POST"])
def editar_cliente(cliente_id):
    if request.method == "GET":
        bd = db.SQLiteConnection('estoque.db')
        bd.connect()
        cliente = bd.execute_query("SELECT * FROM clientes WHERE id = ?;", (cliente_id,))
        return render_template("editar_cliente.html", cliente=cliente)
    elif request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        bd = db.SQLiteConnection('estoque.db')
        bd.connect()
        query = "UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?;"
        bd.execute_query(query, (nome, email, telefone, cliente_id))

        return redirect("/clientes")

@clientes_blueprint.route("/clientes/remover/<int:cliente_id>", methods=["GET"])
def remover_cliente(cliente_id):
    bd = db.SQLiteConnection('estoque.db')
    bd.connect()
    query = "DELETE FROM clientes WHERE id = ?;"
    bd.execute_query(query, (cliente_id,))

    return redirect("/clientes")
