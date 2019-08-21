from flask import  jsonify, request

from uuid import uuid4

class User(object):

    def __init__(self):

        self.users = [
            {
                'id': 1,
                'uuid': uuid4(),
                'nome': 'Gabriel'
            }, {
                'id': 2,
                'uuid': uuid4(),
                'nome': 'João'
            }, {
                'id': 3,
                'uuid': uuid4(),
                'nome': 'Paulo'
            }, {
                'id': 4,
                'uuid': uuid4(),
                'nome': 'Pedro'
            }
        ]


    #seletec all users
    def select_all(self):
        return self.users

    #select user per uuid
    def select_per_uuid(self, uuid):
        for u in self.select_all():
            if str(u['uuid']) == uuid:
                return jsonify(u), 200
        return jsonify({'error': 'not found'}), 404

    #insert user
    def append(self, data):
        newUser = {
            "id" : len(self.users) + 1,
            "uuid": uuid4(),
            "nome": data['nome']
        }
        self.users.append(newUser)
        return jsonify(data), 201

    #update user
    def update(self, uuid):
        for u in self.select_all():
            if u['uuid'] == uuid:
                u['nome'] = request.get_json().get('nome')

                return jsonify(u), 200
        return jsonify({'error': 'user not found'}), 404

    #delete user
    def remove(self, uuid):
        for self.x in self.select_all():
            if str(self.x['uuid']) == str(uuid):
                del self.users[self.x['id'] - 1]
                return jsonify({'message': 'deleted user %s' % str(uuid)}), 200
            else:
                return jsonify({'error': 'user not found'}), 404
