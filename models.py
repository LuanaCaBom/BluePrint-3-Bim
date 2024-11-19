from database import db

class Tecnicos(db.Model):
    __tablename__ = 'tecnico'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(50))

    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def __repr__(self):
        return "<Técnico {}>".format(self.nome)

class Projetos(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    ano_inicio = db.Column(db.Integer)
    id_tecnico = db.Column(db.Integer, db.ForeignKey('tecnico.id'))
    
    tecnico = db.relationship('Tecnicos', foreign_keys=id_tecnico)

    def __init__(self, nome, ano_inicio, id_tecnico):
        self.nome = nome
        self.ano_inicio = ano_inicio
        self.id_tecnico = id_tecnico

    def __repr__(self):
        return "<Projeto {}>".format(self.nome)