from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#Importa os modelos que vamos usar
from app.models.modelos import Casa, Cliente

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



###############################

# Listar Cliente
@app.route("/clientes", methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    lista_clientes = []

    for cliente in clientes:
        # Data de nascimento para o padrão br
        data_nascimento_noNapeBR = cliente.data_nascimento.strftime("%d/%m/%Y") if cliente.data_nascimento else None

        lista_clientes.append({
            'id': cliente.id,
            'nome': cliente.nome,
            'tipo': cliente.tipo,
            'documento': cliente.documento,
            'endereco': cliente.endereco,
            'telefone': cliente.telefone,
            'data_nascimento': data_nascimento_noNapeBR
        })

    return jsonify(lista_clientes)

# Criar Cliente
@app.route("/cliente", methods=['POST'])
def create_cliente():
    dados = request.json
    _nome = dados["nome"]
    _tipo = dados["tipo"]
    _documento = dados["documento"]
    _endereco = dados["endereco"]
    _telefone = dados["telefone"]

    # Convertendo a string de data para um objeto de data Python (formato brasileiro)
    _data_nascimento = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()

    cliente = Cliente(nome=_nome, tipo=_tipo, documento=_documento, endereco=_endereco, telefone=_telefone, data_nascimento=_data_nascimento)
    db.session.add(cliente)
    db.session.commit()

    return jsonify({'status': 201, 'message': 'Cliente criado com sucesso'}), 201

# Atualizar cliente
@app.route("/clientes/<int:cliente_id>", methods=['PUT'])
def update_cliente(cliente_id):
    # Verifica se o cliente existe
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({'status': 404, 'message': 'Cliente não encontrado'}), 404
    
    dados = request.json

    # Atualiza os campos do cliente, se presentes nos dados da solicitação
    cliente.nome = dados.get("nome", cliente.nome)
    cliente.tipo = dados.get("tipo", cliente.tipo)
    cliente.documento = dados.get("documento", cliente.documento)
    cliente.endereco = dados.get("endereco", cliente.endereco)
    cliente.telefone = dados.get("telefone", cliente.telefone)

    # Converte a data de nascimento para um objeto date, se vier na solicitação
    if "data_nascimento" in dados:
        cliente.data_nascimento = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()

    db.session.commit()

    return jsonify({'status': 200, 'message': 'Cliente atualizado com sucesso'}), 200


# Remover Cliente
@app.route("/clientes/<int:cliente_id>", methods=['DELETE'])
def delete_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({'status': 404, 'message': 'Cliente não encontrado'}), 404

    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'status': 200, 'message': 'Cliente deletado com sucesso'}), 200




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