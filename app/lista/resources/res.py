from lista.schemas.ItemSchema import ItemSchema
from lista.models.dao import ItemDao
from flask_restful import Resource, reqparse, abort
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
        json = ''
        try:
            itemDao = ItemDao()
            item = itemDao.encontrar_pelo_nome(item)
            schema = ItemSchema()
            json = schema.dump(item).data
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(item))
        return json,201


    def post(self):
        json = ''
        try:
            data = _item_parser.parse_args()
            nome = data['item']
            itemDao = ItemDao()
            item = itemDao.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(item)}
            else:
                itemDao.adicionar(nome)
                item = itemDao.encontrar_pelo_nome(item)
                schema = ItemSchema()
                json = schema.dump(item).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,item):
        json = ''
        try:
            itemDao = ItemDao()
            item = itemDao.encontrar_pelo_nome(item)
            if item:
                itemDao.remover_pelo_nome(item)
                schema = ItemSchema(many=True)
                json = schema.dump(itemDao.listar()).data
            else:
                abort(404, message="Item {} não está na lista".format(item))
        except Exception as e:
            print(e)
        return json, 204

    def put(self):
        json = ''
        try:
            data = _item_parser.parse_args()
            nome = data['item']
            itemDao = ItemDao()
            item = itemDao.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(item)},200
            else:
                itemDao.adicionar(nome)
                schema = ItemSchema(many=True)
                item = itemDao.encontrar_pelo_nome(nome)
                json = schema.dump(item).data
        except Exception as e:
            print(e)
        return json, 201

class ItemList(Resource):
    def get(self):
        json = []
        try:
            print("ok")
            itemDao = ItemDao()

            lista = itemDao.listar()
            print(lista)
            schema = ItemSchema(many=True)
            json = schema.dump(lista).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201