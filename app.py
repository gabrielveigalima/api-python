from flask import Flask, jsonify, request
from user import User
from todos import ToDos

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

to_dos = ToDos()

# cadastra to-dos
@app.route('/to-dos', methods=['POST'])
def insert_to_dos():
    return to_dos.append(request.get_json())

#retorna todos to-dos
@app.route('/to-dos', methods=['GET'])
def select_all_do_dos():
    return jsonify(to_dos.select_all()), 200

#retorna o to-dos da id
@app.route('/to-dos/<string:uuid>', methods=['GET'])
def select_to_dos_per_id(uuid):
    return to_dos.select_per_uuid(uuid)


# edita to-dos
@app.route('/to-dos/<string:uuid>', methods=['PUT'])
def update_to_dos(uuid):
    return to_dos.update(uuid)


# remove to-dos
@app.route('/to-dos/<string:uuid>', methods=['DELETE'])
def remove_to_dos(uuid):
    return to_dos.delete(uuid)



if __name__ == '__main__':
    app.run(debug=True)