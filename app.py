from flask import Flask, request, render_template, redirect, url_for, jsonify
from database import SQLiteConnection
import json
from cliente import clientes_blueprint
from produtos import produtos_blueprint
from categorias import categorias_blueprint
from usuarios import usuarios_blueprint
from lojas import lojas_blueprint
from fornecedores import fornecedores_blueprint
from permissoes import permissoes_blueprint
from atividades import atividades_blueprint
from vendedores import vendedores_blueprint
import database as db

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
  return render_template("dashboard.html")

@app.route("/logout")
def logout():
  return render_template("login.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")


@app.route("/setup")
def setup():
    try:
        bd = SQLiteConnection('estoque.db')
        bd.connect()

        # Verificando se a tabela categorias existe
        if not SQLiteConnection.table_exists(bd, 'categorias'):
            bd.execute_query("CREATE TABLE categorias (id INTEGER PRIMARY KEY, nome TEXT);")
            bd.execute_query("INSERT INTO categorias VALUES (1, 'Carnes');")
            bd.execute_query("INSERT INTO categorias VALUES (2, 'Gelados');")

        # Verificandop se a tabela clientes existe
        if not SQLiteConnection.table_exists(bd, 'clientes'):
            bd.execute_query('''
                CREATE TABLE clientes (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    tipo TEXT,
                    documento TEXT,
                    endereco TEXT,
                    telefone TEXT,
                    data_nascimento TEXT
                );
            ''')
            bd.execute_query("INSERT INTO clientes VALUES (1, 'Anderson', 'Pessoa Fisica', '000.000.000-00', 'Rua 0, Nº 292', '(87) 999999999', '04/11/1998');")

        bd.disconnect()
        return "Instalado com sucesso!"
    except Exception as e:
        return f"Erro ao Instalar: {str(e)}"
  
#Função temporaria de desenvolvimento para ver as tabelas no banco 
@app.route("/api/tabelas", methods=["GET"])
def listar_tabelas():
    try:
        # Conectar ao banco de dados
        bd = db.SQLiteConnection('estoque.db')
        bd.connect()

        # Consultar tabelas disponíveis
        tabelas = bd.execute_query("SELECT name FROM sqlite_master WHERE type='table';")

        # Retornar a lista de tabelas em formato JSON
        return jsonify(tabelas=[tabela[0] for tabela in tabelas])
    
    #caso ocorra algum erro, e capiturado pela exception e fica mais facil de corrigir
    except Exception as e:
        return jsonify(error=str(e))

app.register_blueprint(clientes_blueprint)
app.register_blueprint(produtos_blueprint)
app.register_blueprint(categorias_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(lojas_blueprint)
app.register_blueprint(fornecedores_blueprint)
app.register_blueprint(permissoes_blueprint)
app.register_blueprint(atividades_blueprint)
app.register_blueprint(vendedores_blueprint)

if __name__ == "__main__":
  app.run(debug=True, port=5000)
