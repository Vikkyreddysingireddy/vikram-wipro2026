from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Wipro"]
collection = db["Employees"]
new_employee = {
    "name": "Abhi",
    "department": "IT",
    "salary": 70000
}
insert_result = collection.insert_one(new_employee)
print("Inserted new employee with ID:", insert_result.inserted_id)

employee = collection.find_one({"_id": insert_result.inserted_id})
print("Details of inserted employee:")
print(employee)
