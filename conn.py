import os
import simplejson
from sqlalchemy import create_engine
import pymysql


class Conn(object):

    def __init__(self):
        # read credentials db
        with open("./Credentials/conn.json") as fh:
            self.red_creds = simplejson.loads(fh.read())

        self.connection_string = "mysql+mysqldb://{user}:{passw}@{host}/{db}".format(user=self.red_creds['user'],
                                                                                           passw=self.red_creds['pass'],
                                                                                           host=self.red_creds['host'],
                                                                                           db=self.red_creds['db'])
        self.db_alias = "{user}@{db}".format(user=self.red_creds['user'], db=self.red_creds['db'])

        pymysql.install_as_MySQLdb()

    def conn(self):
        # create engine
        return create_engine(self.connection_string)


