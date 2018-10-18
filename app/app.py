from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from lista.resources.item import Item,ItemList

app = Flask(__name__)
api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}}) #O uso do cors
api.add_resource(ItemList, '/itens')
api.add_resource(Item, '/item','/item/<string:item>')

if __name__ == '__main__':
    app.run(debug=True)
