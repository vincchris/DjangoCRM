import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '',

)

# Prepare a Cursor Object
cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE db_django_python1")

print("All Done!")