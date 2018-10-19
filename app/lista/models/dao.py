from lista.models.item import Item

class ItemDao:

    def __init__(self):
        item1 = Item(1, "maças")
        item2 = Item(2, "tomates")
        item3 = Item(3, "bananas")
        item4 = Item(4, "leite condensado")
        item5 = Item(5, "bananas")
        self.lista = [item1, item2, item3, item4, item5]

    def adicionar(self,nome):
        lista = [i for i in self.lista if i.nome == nome]
        if not lista:
            item = Item(self.lista.count+1,nome)
            self.lista.append(item)

    def encontrar_pelo_id(self,id):
        lista = [i for i in self.lista if i.id == id]
        return lista[0] if lista else None
    def encontrar_pelo_nome(self,nome):
        lista = [i for i in self.lista if i.nome == nome]
        return lista[0] if lista else None
    def listar(self):
        return self.lista
    def remover_pelo_nome(self,nome):
        lista = [i for i in self.lista if i.nome != nome]
        self.lista = lista
    def remover_pelo_id(self,id):
        lista = [i for i in self.lista if i.id != id]
        self.lista = lista

