import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password'],
    database='wsaa'
)

cursor = db.cursor()
sql = 'select * from student'
# sql = 'select * from student where id = %s'
# sql  = 'describe student'

values = [1]

cursor.execute(sql)
# cursor.execute(sql, values)
result = cursor.fetchall()
for line in result:
    print(result)

cursor.close()
db.close()