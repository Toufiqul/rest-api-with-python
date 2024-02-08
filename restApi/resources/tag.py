from db import db
from models import StoreModel,TagModel,ItemModel
from schemas import TagSchema
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import TagSchema,TagAndItemSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Tags","tags",description="Operations on tags")

@blp.route("/store/<string:store_id>/tag")
class Tag(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()
    
    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        tag = TagModel(**tag_data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag
    
    @blp.response(
        202,
        description="deletes a tab if no item is tagged with the given tag"
        example={"message": "tag deleted"}
    )
    @blp.alt_response(
        404,
        description="tag not found"
    )
    @blp.alt_response(
        400, 
        description="returned if tag has item tagged with it"
    )
    def delete(self, tag_id):
        tag=TagModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "tag deleted"}
        abort(
            400, 
            message="Tag could not be deleted. it has items linked to it"
            )
        
@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(201, TagSchema)
    def ger(self,item_id,tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return tag
    
    @blp.response(201, TagAndItemSchema)
    def ger(self,item_id,tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return {"message": "item removed from database"}