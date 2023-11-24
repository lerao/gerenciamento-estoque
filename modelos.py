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
        
class Lojas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeLoja = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)

    def __init__(self, nomeLoja, endereco, email, cnpj, telefone):
        self.nomeLoja = nomeLoja
        self.endereco = endereco
        self.email = email
        self.cnpj = cnpj
        self.telefone = telefone

    def as_dict(self):
        return {'id': self.id, 'nomeLoja': self.nomeLoja, 'endereco': self.endereco,
                'email': self.email, 'cnpj': self.cnpj, 'telefone': self.telefone}
