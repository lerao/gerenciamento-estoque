###from app import db

# ####################
# Cada classe é uma tabela no banco de dados
# ####################

#Casa herda todas as características de db.Model
#class Casa(db.Model):

    #Propriedades de Casa
   # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  #  qtdQuartos = db.Column(db.Integer)
   # qtdBanheiros = db.Column(db.Integer)
   # rua = db.Column(db.String(100))

    #Construtor, recebendo os parâmetros para adicionar ao objeto
   # def __init__(self, qtdQuartos, qtdBanheiros, rua):
   #     self.qtdQuartos = qtdQuartos
    #    self.qtdBanheiros = qtdBanheiros
    #    self.rua = rua###

##########################################################################################################################################
from app import db

class cliente(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80))
    tipo = db.Colmn(db.String(20))
    documento = db.Column(db.String(19))
    endereco = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    datanascimento = db.Column(db.Date)

    def __init__(self, nome, tipo, documento, endereco, telefone, datanascimento):
        self.nome = nome
        self.tipo = tipo
        self.documento = documento
        self.endereco = endereco
        self.telefone = telefone
        self.datanascimento = datanascimento
