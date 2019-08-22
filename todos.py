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
        query = '''
                        SELECT *
                        FROM todos         			     
                       '''
        self.result_query = self.engine.execute(query)
        todos = []
        for resul in self.result_query:
            todos.append({
                "id": resul[0],
                "uuid": resul[1],
                "description": resul[3],
                "expiration": resul[4],
                "status": resul[5],
                "user": resul[6]
            })

        return todos, 200


    # select to-dos por uuid
    def select_per_uuid(self, uuid):
        query = """SELECT * FROM todos WHERE uuid = '{}' """.format(uuid)
        result_query = self.engine.execute(query)
        try:
            resul = next(result_query)
            todos = {
                "id": resul[0],
                "uuid": resul[1],
                "description": resul[3],
                "expiration": resul[4],
                "status": resul[5],
                "user": resul[6]
            }

            return jsonify(todos), 200

        except StopIteration as ex:
            return jsonify({'error': 'not found'}), 404

        for to in self.select_all():
            if str(to['uuid']) == uuid:
                return jsonify(to), 200
        return jsonify({'error': 'not found'}), 404


    #insert to-dos
    def append(self, data):
        if self.user.select_per_uuid(data['user_uuid'])[1] == 200:
            uuid = uuid4()
            query = """INSERT INTO todos
                                    (uuid,title,description,expiration,status,`user`)
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
        #check if all exist
        if self.select_per_uuid(uuid)[1] == 200:

            query = """UPDATE todos SET description = '{}', expiration = '{}',
                        title = '{}', user = '{}', status = '{}'
                        WHERE uuid = '{}' """.format(request.get_json().get('description'),
                                                     request.get_json().get('expiration'),
                                                     request.get_json().get('title'),
                                                     request.get_json().get('user'),
                                                     request.get_json().get('status'),uuid)

            try:
                result_query = self.engine.execute(query)
                return jsonify({'message': 'update to-dos %s' % str(uuid)}), 200

            except StopIteration as ex:
                return jsonify({'error': ex}), 404

        return jsonify({'error': 'to-dos not found'}), 404




    #remove to-dos
    def delete(self, uuid):
        if self.select_per_uuid(uuid)[1] == 200:
            query = """DELETE FROM todos WHERE uuid = '{}' """.format(uuid)

            try:
                result_query = self.engine.execute(query)
                return jsonify({'message': 'deleted tod-os %s' % str(uuid)}), 200

            except StopIteration as ex:
                return jsonify({'error': ex}), 404

        return jsonify({'error': 'to-dos not found'}), 404