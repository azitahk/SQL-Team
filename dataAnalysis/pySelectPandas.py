#$python -m pip install mysql-connector
import mysql.connector
import pandas as pd

i40db = mysql.connector.connect(
  host="localhost",
  user="I40",
  passwd="Password1",
  database="Industry40db"
)


df = pd.read_sql('SELECT * FROM roomData', con=i40db)

i40db.close()

print(df.head())