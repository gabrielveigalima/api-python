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
        pass

    def append(self, data):

        newTodos = {
            "id": len(self.to_dos) + 1,
            "uuid": uuid4(),
            "title": data['title'],
            "description": data['description'],
            "expiration": data['expiration'],
            "user": data['user_uuid']
        }
        self.to_dos.append(newTodos)
        return jsonify(data), 201

    def update(self, data):
        pass

    def delete(self, uuid):
        pass