from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['flask_server']
users_collection = db['User']


@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    if username and email:
        user = {'username': username, 'email': email}
        users_collection.insert_one(user)
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Missing username or email'}), 400


@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = users_collection.find_one({'username': username}, {'_id': 0})
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/update_user/<username>', methods=['PUT'])
def update_user(username):
    data = request.json
    email = data.get('email')
    result = users_collection.update_one({'username': username}, {'$set': {'email': email}})
    if result.modified_count > 0:
        return jsonify({'message': 'User\'s email updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    result = users_collection.delete_one({'username': username})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)

