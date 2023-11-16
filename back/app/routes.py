"""from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#Importa os modelos que vamos usar
from app.models.modelos import Casa

#CRUD
# Create -> Cria recurso -> POST
# Read -> Ler os recursos -> GET
# Update -> Atualiza um recurso -> PUT
# Delete -> Apaga um recurso -> DELETE

# Read
#Rota que lista todas as casas existes
@app.route("/casa", methods=['GET'])
def get_casas():
    casas = Casa.query.all()
    lista_casas = []
    for casa in casas:
        lista_casas.append({
            'id': casa.id,
            'qtdQuartos': casa.qtdQuartos,
            'qtdBanheiros': casa.qtdBanheiros,
            'rua': casa.rua
            })

    return jsonify(lista_casas)

#Create
# Cria uma casa no banco de dados
@app.route("/casa", methods=['POST'])
def create_casa():
    dados = request.json
    _qtdQuartos = dados["qtdQuartos"]
    _qtdBanheiros = dados["qtdBanheiros"]
    _rua = dados["rua"]

    casa = Casa(qtdQuartos=_qtdQuartos, qtdBanheiros=_qtdBanheiros, rua=_rua)
    db.session.add(casa)
    db.session.commit()
    return jsonify({'status': 201, 'message': 'Casa criada com sucesso'}), 201




# Excluir uma categoria
@app.route('/categoria/<int:categoria_id>', methods=['DELETE'])
def delete_categoria(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    if categoria is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'message': 'Categoria excluída com sucesso'})


# Atualizar uma venda
@app.route('/categoria/<int:categoria_id>', methods=['PUT'])
def update_categoria(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    if categoria is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    data = request.json
    categoria.nome = data['nome']
    categoria.descricao = data['descricao']
    categoria.tipo = data['tipo']
    db.session.commit()
    return jsonify({'message': 'Categoria atualizada com sucesso'})"""


#############################################################################
# ROTAS [CLIENTES]
from flask import Flask, request, jsonify
from app import db, Cliente
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    lista_clientes = []
    data_nascimento_br = cliente.datanascimento.strftime("%d/%m/%Y") if cliente.datanascimento else None
    for cliente in clientes:
        lista_clientes.append({
            'id': cliente.id,
            'nome': cliente.nome,
            'tipo': cliente.tipo,
            'documento': cliente.documento,
            'telefone': cliente.telefone,
            'datanascimento': data_nascimento_br
        })

    return jsonify(lista_clientes)

@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def obter_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return jsonify({
        'id': cliente.id,
        'nome': cliente.nome,
        'tipo': cliente.tipo,
        'documento': cliente.documento,
        'telefone': cliente.telefone,
        'datanascimento': cliente.datanascimento
    })

@app.route('/clientes', methods=['POST'])
def criar_cliente():
    dados_cliente = request.json
    novo_cliente = Cliente(nome=dados_cliente['nome'], tipo=dados_cliente['tipo'], documento=dados_cliente['documento'], endereco=dados_cliente['endereco'], telefone=dados_cliente['telefone'], datanascimento=dados_cliente['datanascimento'])

    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'mensagem': 'Cliente criado com sucesso!'})

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def excluir_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensagem': 'Cliente excluído com sucesso!'})

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente(cliente_id):
     cliente = Cliente.query.get_or_404(cliente_id)
     dados_cliente = request.json

     cliente.nome = dados_cliente.get('nome', cliente.nome)
     cliente.tipo = dados_cliente.get('tipo', cliente.tipo)
     cliente.documento = dados_cliente.get('documento', cliente.documento)
     cliente.endereco = dados_cliente.get('endereco', cliente.endereco)
     cliente.telefone = dados_cliente.get('telefone', cliente.telefone)
     cliente.datanascimento = dados_cliente.get('datanascimento', cliente.datanascimento)

     db.session.commit()
     return jsonify({'mensagem': 'Cliente atualizado com sucesso!'})