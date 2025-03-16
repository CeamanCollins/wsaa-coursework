import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password'],
    database='wsaa'
)

cursor = db.cursor()
sql = 'DELETE FROM student WHERE id = %s'
values = [2]

cursor.execute(sql, values)

db.commit()
print("Deleted!")

cursor.close()
db.close()