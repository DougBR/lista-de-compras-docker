from werkzeug.security import safe_str_cmp
from flask import jsonify
from flask_restful import Resource, abort,reqparse

#ITENS É UMA LISTA DE
LISTA_DE_COMPRAS =  ['feijão','arroz','leite','açúcar','morangos']

_item_parser = reqparse.RequestParser()
_item_parser.add_argument('item',
                          type=str,
                          required=True,
                          help="O nome do Item não pode estar em branco."
                          )



'''
Esta classe representa um recurso na arquitetura REST.
Ela implementa os métodos GET,POST,PUT e DELETE
'''
class Item(Resource):

    def get(self,item):
        if item not in LISTA_DE_COMPRAS:
            abort(404, message="Item {} não está na lista".format(item))
        return {"item":item},200

    def post(self):
        data = _item_parser.parse_args()
        item = data['item']
        if item in LISTA_DE_COMPRAS :
            return {"message":"Item {} já está na lista".format(item)}
        else:
            LISTA_DE_COMPRAS.append(item)
        return item, 201

    def delete(self,item):
        try:
            if item not in LISTA_DE_COMPRAS:
                abort(404, message="Item {} não está na lista".format(item))
            LISTA_DE_COMPRAS.remove(item)
        except Exception as ex:
            print(ex)
            return {"message":"Erro na deleção do item"},500
        return item, 204

    def put(self):
        data = _item_parser.parse_args()
        item = data['item']
        if item in LISTA_DE_COMPRAS :
            return {"message":"Item {} já está na lista".format(item)}
        else:
            LISTA_DE_COMPRAS.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return jsonify(LISTA_DE_COMPRAS)