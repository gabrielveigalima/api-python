from flask import  jsonify, request

class Usuario(object):

    def __init__(self):

        self.users = [
            {
                'id': 1,
                'uuid': '881372e0-361f-4d61-b837-423efda8fee3',
                'nome': 'Gabriel'
            }, {
                'id': 2,
                'nome': 'João'
            }, {
                'id': 3,
                'nome': 'Paulo'
            }, {
                'id': 4,
                'nome': 'Pedro'
            }
        ]


    #lista todoos usuarios
    def select_all(self):
        return self.users

    #adicioan usario

    def append(self, data):
        self.users.append(data)

    def update(self, id):
        for u in self.select_all():
            if u['id'] == id:
                u['nome'] = request.get_json().get('nome')

                return jsonify(u), 200
        return jsonify({'error': 'user not found'}), 404

    def remove(self, id):

        self.users[id - 1] = {
            "id": id,
            "status": "DELETED"
        }
        return True
