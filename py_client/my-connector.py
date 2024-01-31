import mysql.connector
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
# Параметри підключення до OLTP системи
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    port='3306',
    database='mydb'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM grade')
person = mycursor.fetchall()
for i in person:
    print(i)
url = 'mysql://root:root@127.0.0.1:3306/mydb'
engine = create_engine(url,
                       echo=False,
                       pool_size=5,
                       max_overflow=10
)

with engine.connect() as conn:
    res=conn.execute(text("SELECT VERSION()"))
    print(f"{res}")

