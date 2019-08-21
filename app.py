from flask import Flask, jsonify, request
from user import User

app = Flask(__name__)

#Pagina inicial
@app.route('/')
def home():
    return 'Hello, world!!', 200


# ROTAS DE USUÁRIOS

user = User()

#retorna todos usuarios
@app.route('/users', methods=['GET'])
def select_all_users():
    return jsonify(user.select_all()), 200

#retorna o usuario da id
@app.route('/user/<string:uuid>', methods=['GET'])
def select_users_per_id(uuid):
    return user.select_per_uuid(uuid)

# cadastra usuario
@app.route('/user', methods=['POST'])
def insert_user():
    return user.append(request.get_json())

# edita usuario
@app.route('/user/<string:uuid>', methods=['PUT'])
def update_user(uuid):
    return user.update(uuid)

# remove usuario
@app.route('/user/<string:uuid>', methods=['DELETE'])
def remove_user(uuid):
    return user.remove(uuid)

# FIM ROTAS DE USUÁRIOS


# ROTAS TO-DOS
@app.route('/to-dos')
def to_dos_hello():
    return 'Hello, world!!', 200


if __name__ == '__main__':
    app.run(debug=True)