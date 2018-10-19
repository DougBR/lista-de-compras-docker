from datetime import datetime
class Item(object):
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome
        self.dataCriacao = datetime.now()