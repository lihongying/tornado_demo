#coding:utf-8
import tornado
import tornado.web
import MySQLdb
import database_conf
from base_handler import BaseHandler

class UserHandler(BaseHandler):

    def get(self, *args, **kwargs):
        sql= "select * from user"
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql)
        users = cursor.fetchall()
        cursor.close()
        con.close()

        result={"status": "success", "results": list(users)}

        return self.write(result)

    def post(self, *args, **kwargs):
        pass


