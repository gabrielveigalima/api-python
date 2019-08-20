from flask import Flask, jsonify, request
import usuarios

app = Flask(__name__)


#Pagina inicial
@app.route('/')
def home():
    return 'Hello, world!!', 200

#retorna todos usuarios
@app.route('/usuarios', methods=['GET'])
def all_users():
    return jsonify(usuarios.all_users()), 200

#retorna o usuario da id
@app.route('/usuarios/<int:id>', methods=['GET'])
def select_users_per_id(id):
    for u in usuarios.all_users():
        if u['id'] == id:
            return jsonify(u), 200

    return jsonify({'error': 'not found'}), 404

# cadastra usuario
@app.route('/usuarios', methods=['POST'])
def add_user():
    data = request.get_json()
    usuarios.append(data)
    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True)