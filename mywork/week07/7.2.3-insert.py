import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password'],
    database='wsaa'
)

cursor = db.cursor()
sql = 'INSERT INTO student (firstname, age) VALUES (%s, %s)'
values = ['Mary', 26]

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

cursor.close()
db.close()