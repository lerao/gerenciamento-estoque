from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#Importa os modelos que vamos usar
from app.models.modelos import Casa, Tarefa

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


"""

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
    return jsonify({'message': 'Categoria atualizada com sucesso'})
"""

#===== Lista as tarefas =====
@app.route("/tarefa", methods=['GET'])
def lista_tarefas():
    tarefas = Tarefa.query.all()
    lista_tarefa = []

    for tarefa in tarefas:
        lista_tarefa.append({
            'id': tarefa.id,
            'descricao': tarefa.descricao,
            'status': tarefa.status
        })

    return jsonify({'tarefas': lista_tarefa})


#===== Cria as tarefas =====
@app.route("/tarefa", methods=['POST'])
def criar_tarefa():
    from app import db
    dados = request.json

    if 'descricao' not in dados:
        return jsonify({'status': 400, 'message': 'Descrição da tarefa é obrigatória'}), 400

    descricao = dados['descricao']
    nova_tarefa = Tarefa(descricao=descricao)

    db.session.add(nova_tarefa)
    db.session.commit()

    return jsonify({'status': 201, 'message': 'Tarefa criada com sucesso'}), 201