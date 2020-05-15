import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="openfoodfact"
)

mycursor = mydb.cursor()

for x in mycursor:
  print(x)

print(mydb)