import mariadb
import config

db = mariadb.connect(
    host=config.sql['host'],
    user=config.sql['username'],
    password=config.sql['password']
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE wsaa")

cursor.close()
db.close()