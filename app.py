from flask import Flask, jsonify
import usuarios

app = Flask(__name__)



@app.route('/')
def home():
    return 'Hello, world!!', 200

@app.route('/usuarios', methods=['GET'])
def all_users():
    return jsonify(usuarios.all_users()), 200


if __name__ == '__main__':
    app.run(debug=True)