from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}
@app.route('/')
def home():
    return "User API is running!"
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return {"error": "User not found"}, 404
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data['id']
    
    users[user_id] = {
        "name": data['name'],
        "age": data['age']
    }
    
    return {"message": "User added successfully"}
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id]['name'] = data.get('name', users[user_id]['name'])
        users[user_id]['age'] = data.get('age', users[user_id]['age'])
        
        return {"message": "User updated"}
    return {"error": "User not found"}, 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return {"message": "User deleted"}
    return {"error": "User not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)