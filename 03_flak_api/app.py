from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': "My store",
        'items' :[
            {
                'name': 'My Item',
                'price':15.99
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_data = {
        'name':request_data['name'],
        'items': []
    }
    stores.append(new_data)
    return jsonify(new_data)


#GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://localhost:8080/some_name'
def get_store(name):
    # Iterate over stores and when the store name matches return the store
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message':'No store found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'no store found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'no store found'})

app.run(port=8080)