import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhinay@123",
    database="Company_DB"
)

cursor = conn.cursor()
print("Connected to database successfully!")

print("\nEmployees with salary > 50000:")
query1 = "SELECT * FROM Employees WHERE Salary > 50000"
cursor.execute(query1)

for row in cursor.fetchall():
    print(row)

insert_query = """
INSERT INTO Employees (Name, Department, Salary)
VALUES (%s, %s, %s)
"""
new_employee = ("Teja", "IT", 65000)
cursor.execute(insert_query, new_employee)
conn.commit()

print("New employee inserted successfully!")

update_query = """
UPDATE Employees
SET Salary = Salary * 1.10
WHERE Name = %s
"""
cursor.execute(update_query, ("Teja",))
conn.commit()

print("Salary updated by 10% successfully!")

cursor.close()
conn.close()
print("Database connection closed.")
