from flask import  jsonify, request

from uuid import uuid4
from conn import Conn
class User(object):

    def __init__(self):

        conn = Conn()
        self.engine = conn.conn()


    #seletec all users
    def select_all(self):
        query = '''
                 SELECT *
                 FROM users         			     
                '''
        self.result_query = self.engine.execute(query)
        users = []
        for x in self.result_query:
            users.append({
                 "id": x[0],
                 "uuid": x[1],
                 "name": x[2],
             })

        return users, 200

    #select user per uuid
    def select_per_uuid(self, uuid):
        query = """SELECT * FROM users WHERE uuid = '{}' """.format(uuid)
        result_query = self.engine.execute(query)
        try:
            resul =  next(result_query)
            user = {
                "id": resul[0],
                "uuid": resul[1],
                "name": resul[2]
            }

            return jsonify(user), 200

        except StopIteration as ex:
            return jsonify({'error': 'not found'}), 404

    #insert user
    def append(self, data):
        uuid = uuid4()
        query = """INSERT INTO users
                        (uuid,name)
                    VALUES 
                        ('{}','{}') """.format(uuid,data['nome'])
        try:
            result_query = self.engine.execute(query)
            user = {
                "uuid": uuid,
                "name": data['nome']
            }

            return user, 201

        except StopIteration as ex:
            return jsonify({'error': ex}), 404

    #update user
    def update(self, uuid):
        if self.select_per_uuid(uuid)[1] == 200:
            name = request.get_json().get('name')
            query = """UPDATE users SET name = '{}' WHERE uuid = '{}' """.format(name,uuid)

            try:
                result_query = self.engine.execute(query)
                return jsonify({'message': 'update user %s' % str(uuid)}), 200, 200

            except StopIteration as ex:
                return jsonify({'error': ex}), 404


    #delete user
    def remove(self, uuid):
        
        if self.select_per_uuid(uuid)[1] == 200:
            query = """DELETE FROM users WHERE uuid = '{}' """.format( uuid)

            try:
                result_query = self.engine.execute(query)
                return jsonify({'message': 'deleted user %s' % str(uuid)}), 200

            except StopIteration as ex:
                return jsonify({'error': ex}), 404


