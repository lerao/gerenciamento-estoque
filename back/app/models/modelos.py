from app import db

# ####################
# Cada classe é uma tabela no banco de dados
# ####################

#Casa herda todas as características de db.Model
class Casa(db.Model):

    #Propriedades de Casa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtdQuartos = db.Column(db.Integer)
    qtdBanheiros = db.Column(db.Integer)
    rua = db.Column(db.String(100))

    #Construtor, recebendo os parâmetros para adicionar ao objeto
    def __init__(self, qtdQuartos, qtdBanheiros, rua):
        self.qtdQuartos = qtdQuartos
        self.qtdBanheiros = qtdBanheiros
        self.rua = rua



###################################  Projeto  ###############################################

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    documento = db.Column(db.String(16), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, tipo, documento, endereco, telefone, data_nascimento):
        self.nome = nome
        self.tipo = tipo
        self.documento = documento
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento


#======== Tabela Tarefa =========
class Tarefa(db.Model):
    # Propriedades de Tarefa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='Pendente')

    def __init__(self, descricao):
        self.descricao = descricao