from flask import Flask, request
from db import items,stores
from flask_smorest import abort
import uuid

app = Flask(__name__)


@app.get("/store")  #http://127.0.0.1:5000/store
def get_store():
    return {"stores":list(stores.values())}

@app.post("/store") #http://127.0.0.1:5000/store
def create_store():
    store_data = request.get_json() #request is the body sent in the post request. comes from flask. import from flask
    if "name" not in store_data:
        abort(404, message="Please include 'name' in the json payload.")
    for store in stores.values():
        if store_data["name"]==store["name"]:
            abort(404, message="Store already exists.")

    store_id=uuid.uuid4().hex
    new_store = {**store_data,"id":store_id    }
    stores[store_id] = new_store
    return new_store,201 #201 is the return status code

@app.post("/item") #grabbing the store name. whatever text comes after store/
def create_item():
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            404,
            message = "Bad request. Please ensure 'price' 'store_id' and 'name' are present in the json payload"
        )#aborts the request and returns error code with message
    for item in item.values():
        if(
            item_data["name"]==item["name"]
            and item_data["store_id"]==item["store_id"]
        ):
            abort(404, message="Item already exists")
    if item_data["store_id"] not in stores:
        abort(404,message = "store not found.")

    item_id=uuid.uuid4().hex
    new_item = {**item_data,"id":item_id}
    items[item_id] = new_item
    return new_item,201

@app.get("/items")
def get_all_items():
    return {"items":list(items.values())}

@app.get("/store/<string:store_id>")
def get_store_name(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message = "store not found.")
    
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message = "item not found.")