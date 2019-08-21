from uuid import uuid4
from flask import jsonify, request
from user import User


#TO-DOS
class ToDos(object):

    def __init__(self):
        self.to_dos = []
        self.user = User()

    def select_all(self):
        return self.to_dos

    def select_per_uuid(self, uuid):
        for to in self.select_all():
            if str(to['uuid']) == uuid:
                return jsonify(to), 200
        return jsonify({'error': 'not found'}), 404

    def append(self, data):

        newTodos = {
            "id": len(self.to_dos) + 1,
            "uuid": uuid4(),
            "title": data['title'],
            "description": data['description'],
            "expiration": data['expiration'],
            "status": data['status'],
            "user": data['user_uuid']
        }
        self.to_dos.append(newTodos)
        return jsonify(data), 201

    def update(self, uuid):
        for to in self.select_all():
            if str(to['uuid']) == uuid:
                to['description'] = request.get_json().get('description')
                to['expiration'] = request.get_json().get('expiration')
                to['title'] = request.get_json().get('title')
                to['user'] = request.get_json().get('user')
                to['status'] = request.get_json().get('status')

                return jsonify(to), 200
        return jsonify({'error': 'to-dos not found'}), 404

    def delete(self, uuid):
        for self.x in self.select_all():
            if str(self.x['uuid']) == str(uuid):
                del self.to_dos[self.x['id'] - 1]
                return jsonify({'message': 'deleted to-dos %s' % str(uuid)}), 200
            else:
                return jsonify({'error': 'to-dos not found'}), 404