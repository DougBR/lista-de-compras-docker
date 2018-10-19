from marshmallow import Schema,fields
from lista.models.item import Item

class ItemSchema(Schema):
    nome = fields.Str()
    id = fields.Integer()
    dataCriacao = fields.DateTime()
    class Meta:
        model = Item