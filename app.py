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
def select_users_per_id(uuid):
    for u in usuario.select_all():
        if u['id'] == uuid:
            return jsonify(u), 200
    return jsonify({'error': 'not found'}), 404

# cadastra usuario
@app.route('/user', methods=['POST'])
def insert_user():
    return usuario.append(request.get_json())

# edita usuario
@app.route('/user/<string:uuid>', methods=['PUT'])
def update_user(uuid):
    return usuario.update(uuid)

# remove usuario
@app.route('/user/<string:uuid>', methods=['DELETE'])
def remove_user(uuid):
    return usuario.remove(uuid)

if __name__ == '__main__':
    app.run(debug=True)