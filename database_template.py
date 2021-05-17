# Fill in the password of your database and rename this file to "database.py"
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='', # the password of the database
    database='school' # the name of the database
)