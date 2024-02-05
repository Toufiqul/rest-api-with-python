from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name":"generic store",
        "items":[
            {
                "name":"apple",
                "price":10
            },
            {
                "name":"banana",
                "price":20
            }
        ]
    }
]

@app.get("/store")  #http://127.0.0.1:5000/store
def get_store():
    return {"stores":stores}

@app.post("/store") #http://127.0.0.1:5000/store
def create_store():
    request_data = request.get_json() #request is the body sent in the post request. comes from flask. import from flask

    new_store = {
        "name":request_data["name"],
        "items":request_data["items"]
    }
    stores.append(new_store)
    return new_store,201 #201 is the return status code

@app.post("/store/<string:name>/item") #grabbing the store name. whatever text comes after store/
def create_item(name):
    request_data = request.get_json()
    new_item = {'name': request_data['name'],'price': request_data['price']}
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return new_item,201
    return {'error':'store not found'},404

@app.get("/store/<string:name>")
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return store,201
    return {'error':'store not found'},404