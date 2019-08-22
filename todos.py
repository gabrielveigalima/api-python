from uuid import uuid4
from flask import jsonify, request
from user import User
from conn import Conn


#TO-DOS
class ToDos(object):

    def __init__(self):
        self.user = User()
        conn = Conn()
        self.engine = conn.conn()

    #select all to-dos
    def select_all(self):
        return self.to_dos

    # select to-dos por uuid
    def select_per_uuid(self, uuid):
        for to in self.select_all():
            if str(to['uuid']) == uuid:
                return jsonify(to), 200
        return jsonify({'error': 'not found'}), 404


    #insert to-dos
    def append(self, data):


        if self.user.select_per_uuid(data['user_uuid'])[1] == 200:
            uuid = uuid4()
            query = """INSERT INTO todos
                                    (uuid,title,description,expiration,status,user)
                                VALUES 
                                    ('{}','{}','{}','{}','{}','{}') """.format(uuid, data['title'],
                                                                               data['description'], data['expiration'],
                                                                               data['status'], data['user_uuid'])
            try:
                result_query = self.engine.execute(query)
                todos = {

                    "uuid": uuid,
                    "title": data['title'],
                    "description": data['description'],
                    "expiration": data['expiration'],
                    "status": data['status'],
                    "user": data['user_uuid']
                }

                return todos, 201

            except StopIteration as ex:
                return jsonify({'error': ex}), 404
        return jsonify({'error': 'user not found'}), 404
    #update to-dos
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


    #remove to-dos
    def delete(self, uuid):
        for self.x in self.select_all():
            if str(self.x['uuid']) == str(uuid):
                del self.to_dos[self.x['id'] - 1]
                return jsonify({'message': 'deleted to-dos %s' % str(uuid)}), 200
            else:
                return jsonify({'error': 'to-dos not found'}), 404