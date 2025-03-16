import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password'],
    database='wsaa'
)

cursor = db.cursor()

cursor.execute("CREATE TABLE student (id int NOT NULL auto_increment, firstname varchar(100), age int, PRIMARY KEY(id));")

cursor.close()
db.close()