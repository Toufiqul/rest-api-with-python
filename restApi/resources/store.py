import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema

from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from db import db
from models import StoreModel

blp = Blueprint("Stores", "stores", description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(cls, store_id):
            store = StoreModel.query.get_or_404(store_id) #quesry comes from flask SQLAlchemy. doesn't exist in just SQLAlchemy
            return store
    def delete(cls, store_id):
            item = StoreModel.query.get_or_404(store_id)
            raise NotImplementedError("will implement delete store later")



@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Store already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting data")
        return store