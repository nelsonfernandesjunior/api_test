import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*": {"origins": "*"}})

devs = [
    {
        'id': 1,
        'name': 'Bill Gates',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Robert De Niro',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'Steve Jobs',
        'lang': 'ruby'
    },
    {
        'id': 4,
        'name': 'Paul Newmann',
        'lang': 'python'
    },
    {
        'id': 5,
        'name': 'Caption Kirk',
        'lang': 'node'
    }
]


@app.route('/')
def index():
    return "<h1>API REST by Nelson Fernandes - Automation Testing</h1>"


@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200


@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    if dev in devs:
        dev['lang'] = request.get_json().get('lang')
        return jsonify(dev), 200
    return jsonify({'error': 'dev not found'}), 404


@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error': 'not found'}), 404


@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201


@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    index = id - 1
    del devs[index]
    return jsonify({'message': 'Dev removed'}), 200


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    main()
