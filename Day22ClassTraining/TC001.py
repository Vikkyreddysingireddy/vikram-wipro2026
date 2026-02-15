import mysql.connector
host="localhost"
user="root"
password="Abhinay@123"
database="Feb_2026"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

query="SELECT * FROM employee"
cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)