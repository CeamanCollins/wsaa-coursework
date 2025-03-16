import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password'],
    database='wsaa'
)

cursor = db.cursor()
sql = 'UPDATE student set firstname= %s, age = %s WHERE id = %s'
values = ['Maria', 29, 4]

cursor.execute(sql, values)

db.commit()
print("Updated")

cursor.close()
db.close()