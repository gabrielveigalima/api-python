from flask import Flask, jsonify, request
from usuarios import Usuario

app = Flask(__name__)

usuario = Usuario()
#Pagina inicial
@app.route('/')
def home():
    return 'Hello, world!!', 200

#retorna todos usuarios
@app.route('/users', methods=['GET'])
def select_all_users():
    return jsonify(usuario.select_all()), 200

#retorna o usuario da id
@app.route('/user/<int:id>', methods=['GET'])
def select_users_per_id(id):
    for u in usuario.select_all():
        if u['id'] == id:
            return jsonify(u), 200

    return jsonify({'error': 'not found'}), 404

# cadastra usuario
@app.route('/user', methods=['POST'])
def insert_user():
    data = request.get_json()
    usuario.append(data)
    return jsonify(data), 201

# edita usuario
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    return usuario.update(id)

# remove usuario
@app.route('/user/<int:id>', methods=['DELETE'])
def remove_user(id):
    if usuario.remove(id):
        return jsonify({'message': 'deleted user %d' % id}), 200
    else:
        return jsonify({'error': 'user not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)