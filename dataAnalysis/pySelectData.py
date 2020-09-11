#$python -m pip install mysql-connector
import mysql.connector

i40db = mysql.connector.connect(
  host="localhost",
  user="I40",
  passwd="Password1",
  database="Industry40db"
)

#print(i40db)

i40cursor = i40db.cursor()
i40cursor.execute("SELECT * FROM roomData")
resultSet = i40cursor.fetchall()





for x in resultSet:
  print(x)


i40db.close()

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html