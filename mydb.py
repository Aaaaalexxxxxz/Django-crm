# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "20050807"
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrmdatabase")

print("Database created successfully........")