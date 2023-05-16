import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'Ahmad',
    password = 'zxzc',

)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")