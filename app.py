from flask import Flask, jsonify, request

app = Flask(__name__)

plants = [
    {'nama' : "terong",
    'jenis' : "buah"
    }
]

@app.route('/tanaman')
def hello():
    return jsonify(plants)

@app.route('/tanaman/<int:index>', methods=['GET'])
def get_plants(index):

    return jsonify(plants[index]), 200

@app.route('/tanaman', methods=['POST'])
def add_plants():
    plant = request.get_json()
    plants.append(plant)
    return {'id': len(plants)}, 200

@app.route('/tanaman/<int:index>', methods=['PUT'])
def update_plants(index):
    plant = request.get_json()
    plants[index] =  plant
    return jsonify(plants[index]), 200

@app.route('/tanaman/<int:index>', methods=['DELETE'])
def delete_plants(index):
    plants.pop(index)
    return jsonify({
        'id' : index,
        'status': 'deleted'
    }), 200

app.run()