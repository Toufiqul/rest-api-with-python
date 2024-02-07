import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            return item
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
            item = ItemModel.query.get_or_404(item_id)
            raise NotImplementedError("will implement delete item later")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
            item = ItemModel.query.get(item_id)
            if item:
                 item.price=item_data["price"]
                 item.name=item_data["name"]
            else:
                 item = ItemModel(id= item_id,**item_data)
            db.session.add(item)
            db.session.commit()

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting data")
        return item