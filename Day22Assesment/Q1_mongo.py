from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]
collection.delete_many({})

employee = {
    "name": "Abhi",
    "department": "IT",
    "salary": 65000
}

collection.insert_one(employee)
print("Employee inserted into MongoDB.")

collection.update_one(
    {"name": "Abhi"},
    {"$set": {"salary": 70000}}
)

print("Salary updated for Abhi.")

print("Employees in IT department:")

it_employees = collection.find({"department": "IT"})

for emp in it_employees:
    print(emp)
