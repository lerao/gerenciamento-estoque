
from flask import Flask, render_template, request, redirect, Blueprint;
import database as db;

fornecedores_blueprint = Blueprint('fornecedores', __name__)

@fornecedores_blueprint.route("/fornecedores")
def fornecedores():
  return render_template("erro.html")
@fornecedores_blueprint.route("/fornecedores")
def listar_fornecedores():
  bd =db.SQLiteConnection('fornecedores.db')
  bd.connect
  fornecedores = bd.execute_query("SELECT * FROM FORNECEDORES;")
  return render_template("fornecedores.html", dados=fornecedores)

@fornecedores_blueprint.route("/fornecedores/adicionar", methods=["POST"])
def adicionar_fornecedor():
  if request.method =="POST":
    nome = request.form.get('nome')
    cnpj = request.form.get('cnpj')
    fantasia = request.form.get('fantasia')
    contato = request.form.get('contato')
    endereco  = request.form.get('endereco')
    
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  query = "INSERT INT fornecedores (nome, cnpj, fantasia, contato, endereco) VALUES (?,?,?)"
  bd.execute_query(query,(nome,cnpj,fantasia,contato,endereco)) 
  return redirect("/fornecedores")

@fornecedores_blueprint.route("/fornecedores/editar/<int:cliente_id", methods=["GET","POST"])
def editar_fornecedor(fornecedores_id):
    if request.method == "GET":
      bd = db.SQLiteConnection('estoque.db')
      bd.connect()
      fornecedores = bd.execute_query("SELECT * FROM fornecedores WHERE id = ?;", (fornecedores_id))
      return render_template("editar_fornecedores.html", fornecedores=fornecedores)
    elif request.method("POST"):
      nome = request.form.get('nome')
      cnpj = request.form.get('cnpj')
      fantasia = request.form.get('fantasia')
      contato = request.form.get('contato')
      endereco = request.form.get('endereco')
      
      bd = db.SQLiteConnection('fornecedores.db')
      bd.connect()
      query = "UPDATE fornecedores SET nome = ?.cnpj = ?, fantasia = ?, contato = ?, endereco =? WHERE id = ? ;"
      bd.execute_query(query,(nome,cnpj,fantasia,contato,endereco, fornecedores_id))
      
      return redirect("/fornecedores")
    
@fornecedores_blueprint.route("/fornecedores/remover/<int:fornecedores_id>", methods=["GET"])
def remover_fornecedores(fornecedores_id):
    bd = db.SQLiteConnection('estoque.db')
    bd.connect()
    query = "DELETE FROM fornecedores WHERE id = ?;"
    bd.execute_query(query, (fornecedores_id,))

    return redirect("/fornecedores")         
