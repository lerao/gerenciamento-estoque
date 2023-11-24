from flask import request, jsonify, make_response, render_template, redirect, url_for
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime



#Importa os modelos que vamos usar
from app.models.modelos import Casa
from app.models.modelos import Atividade

#CRUD
# Create -> Cria recurso -> POST
# Read -> Ler os recursos -> GET
# Update -> Atualiza um recurso -> PUT
# Delete -> Apaga um recurso -> DELETE

# Read
#Rota que lista todas as casas existes

@app.route("/")
def index():
  return render_template("login.html")

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

@app.route('/novaAtividade', methods=['POST', 'GET'])
def novaAtividade():
    atividades=None
    if request.method=='POST':
   
        nome = request.form['nomeAtividade']
        status = request.form['status']

        atividade = Atividade(nome=nome, status=status)
        db.session.add(atividade)
        db.session.commit()
        return redirect('/listaAtividade')
        #return jsonify({'status': 201, 'message': 'Atividade criada com sucesso'}), 201
   
    return render_template('/atividade.html', atividades=atividades)

@app.route('/listaAtividade', methods=["GET"])
def listaAtividade():
    atividades = Atividade.query.all()
    print("atividades: ", atividades)
    return render_template("/atividade.html", atividades=atividades)


@app.route('/editAtividade/<int:id>', methods=['POST', 'GET'])
def editAtividade(id):
    print("id da atividade a ser editada",id)
    atividade = Atividade.query.get_or_404(id)  # Encontra a atividade pelo ID ou retorna um erro 404 se não existir
    print(atividade)
    if request.method == 'POST':
        atividade.nome = request.form['nomeAtividade']  
        atividade.status = request.form['status']  
        db.session.commit()

        return redirect(url_for('listaAtividade'))
   
   
    return render_template('atividade_editar.html', atividades=atividade)

@app.route('/del_atividade/<int:id>', methods=['POST','GET'])
def del_atividade(id):
    atividade = Atividade.query.get_or_404(id)  
    db.session.delete(atividade)  
    db.session.commit()  
    return redirect(url_for('listaAtividade'))  

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