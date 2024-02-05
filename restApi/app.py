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