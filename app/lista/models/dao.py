from lista.models.item import Item
from werkzeug.security import safe_str_cmp
class ItemDao:
    item1 = Item(1, "maças")
    item2 = Item(2, "tomates")
    item3 = Item(3, "bananas")
    item4 = Item(4, "leite condensado")
    item5 = Item(5, "peras")
    indice = 5
    LISTA = [item1,item2,item3,item4,item5]

    @classmethod
    def adicionar(cls,nome):
        lista = [i for i in cls.LISTA if i.nome == nome]
        if not lista:
            cls.indice = cls.indice + 1
            item = Item(cls.indice,nome)
            cls.LISTA.append(item)

    @classmethod
    def encontrar_pelo_id(cls,id):
        lista = [i for i in cls.LISTA if i.id == id]
        return lista[0] if lista else None

    @classmethod
    def encontrar_pelo_nome(cls,nome):
        lista = [i for i in cls.LISTA if i.nome == nome]

        if len(lista) > 0:
            return lista[0]
        else:
            return None

    @classmethod
    def listar(cls):
        return cls.LISTA

    @classmethod
    def remover_pelo_nome(cls,nome):
        lista = [i for i in cls.LISTA if i.nome != nome]
        cls.LISTA = lista


    @classmethod
    def remover_pelo_id(cls,id):
        lista = [i for i in cls.LISTA if i.id != id]
        cls.LISTA = lista

