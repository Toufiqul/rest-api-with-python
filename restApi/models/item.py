from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer,db.ForeignKey("stores.id"), unique=False, nullable=False) #db.ForeignKey("stores.id") to specify stores table's id is a foreign key in items table
    store = db.relationship("StoreModel",back_populates = "items")
    # SQLAlchemy knows that the stores table is used by the StoreModelclass. So, when we have a store_id that is using the stores table, we can then define a relationship with the StoreModelclass, and it will automatically populate the store variable with a StoreModel object whose id matches that of theForeignKey. This is pretty handy, because it will mean that when we have an ItemModelobject, we can just say my_item.store,and that will be a StoreModelobject that is associated with the item.back_populates="items" is going to be used, so that the StoreModel class will also have an items relationship here that allows each StoreModel object to see very easily all of the items that areassociated with it.
    tags = db.relationship("TagModel",back_populates = "items",secondary="item_tags")