import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='4jnstH!&GVTMA35!UTGkYDtA',
    database='school'
)

cursor = db.cursor()
cursor.execute("show tables")

TABLES = [table[0 ]for table in cursor.fetchall()]