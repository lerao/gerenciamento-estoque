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


# Tabela tarefa
class Tarefa(db.Model):
    # Propriedades de Tarefa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='Pendente')

    def __init__(self, descricao):
        self.descricao = descricao