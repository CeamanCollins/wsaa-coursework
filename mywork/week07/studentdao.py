# import mysql.connector
import mariadb
import config

class StudentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor =""
    def __init__(self):
        self.host=config.sql['host']
        self.user=config.sql['username']
        self.password=config.sql['password']
        self.database="wsaa"
    def getCursor(self):
        # self.connection = mysql.connector.connect(
        self.connection = mariadb.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into student (firstname, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result
    def findByID(self, id):
        cursor = self.getCursor()
        sql = "select * from student where id=%d"
        values = [id]
        cursor.execute(sql,values)
        result = cursor.fetchall()
        self.closeAll()
        return result 
    def update(self, values):
        cursor = self.getCursor()
        sql = "UPDATE student SET firstname= %s, age = %s WHERE id = %s"
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return "Update done!"
    def delete(self, id):
        cursor = self.getCursor()
        sql = "DELETE FROM student WHERE id = %s"
        values = [id]
        cursor.execute(sql,values)
        self.closeAll()
        return "Deleted"

studentDAO = StudentDAO()

