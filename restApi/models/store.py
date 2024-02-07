from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    items = db.relationship("ItemModel",back_populates="store",lazy="dynamic")
    #you'llnotice that there is no item_id in thisStoreModel, but we've got this ItemModelrelationship. This store back_populatesto "items", and here the itemsback_populates to store. SQLAlchemy knowsthat these are two ends of a relationship.Therefore, the item has a store_id, whichis what links one item to one store, andit will know the items is the other end ofthat relationship, and therefore topopulate this variable, it needs to gointo the items table and find all theitems that have a store_id equal to thisstore's id. lazy="dynamic" means it's only populated when it is called.