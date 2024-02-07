from db import db

class ItemModle(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.String(100), nullable=False)