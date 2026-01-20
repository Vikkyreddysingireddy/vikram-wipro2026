class PositiveSalary:
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number.")
        instance.__dict__['salary'] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get('salary')

class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("laddu", 50000)
emp2 = Employee("vikky", 75000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

try:
    emp3 = Employee("abcd", -30000)
except ValueError as e:
    print("Error:", e)
