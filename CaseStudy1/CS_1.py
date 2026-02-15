import json
import csv
from abc import ABC, abstractmethod

def log_method(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("[LOG] Method", func.__name__, "executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(self, *args, **kwargs)
    return wrapper


class Marks:
    def __get__(self, obj, objtype=None):
        return obj._marks

    def __set__(self, obj, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Error: Marks should be between 0 and 100")
        obj._marks = value


class Salary:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value

class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass

class Student(Person):
    marks = Marks()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def __del__(self):
        print("Student object deleted")

    def get_details(self):
        print("Student Details")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    @log_method
    def calculate_performance(self):
        total = sum(self.marks)
        avg = total / len(self.marks)

        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"

        print("Student Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg, 1))
        print("Grade        :", grade)

        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()


class Faculty(Person):
    salary = Salary()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary
        self.is_admin = False

    def get_details(self):
        print("Faculty Details")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)

    def calculate_performance(self):
        pass


class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


def student_generator(students):
    print("Fetching Student Records...")
    for s in students:
        yield s


def save_students_json(students):
    data = []
    for s in students:
        avg = sum(s.marks) / len(s.marks)
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "average": round(avg, 1)
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student data successfully saved to students.json")


def save_students_csv(students):
    with open("students_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
            writer.writerow([s.id, s.name, s.department, round(avg, 1), grade])

    print("CSV Report generated")


try:
    s1 = Student("S101", "Abhi", "Computer Science", 4, [78, 85, 90, 88, 92])
    s2 = Student("S102", "Sai", "Computer Science", 4, [70, 75, 80, 85, 90])

    print("Student Created Successfully")
    print("--------------------------------")
    print("ID        :", s1.id)
    print("Name      :", s1.name)
    print("Department:", s1.department)
    print("Semester  :", s1.semester)

    f1 = Faculty("F201", "Dr. Hari", "Computer Science", 50000)

    print("Faculty Created Successfully")
    print("--------------------------------")
    print("ID        :", f1.id)
    print("Name      :", f1.name)
    print("Department:", f1.department)

    c1 = Course("CS401", "Data Science", 4, f1)
    c2 = Course("CS402", "Python", 3, f1)

    print("Course Added Successfully")
    print("--------------------------------")
    print("Course Code :", c1.code)
    print("Course Name :", c1.name)
    print("Credits     :", c1.credits)
    print("Faculty     :", f1.name)

    print("Enrollment Successful")
    print("--------------------------------")
    print("Student Name :", s1.name)
    print("Course       :", c1.name)

    print()
    s1.calculate_performance()

    print("Polymorphism Output")
    s1.get_details()
    f1.get_details()

    print("Compare Two Students")
    print("Abhi > Sai :", s1 > s2)

    print("Merge Course Credits")
    print("Total Credits After Merge :", c1 + c2)

    print("Student Record Generator")
    print("--------------------------------")
    for student in student_generator([s1, s2]):
        print(student.id, "-", student.name)

    save_students_csv([s1])
    save_students_json([s1])

except ValueError as e:
    print("Invalid Marks")
    print(e)

except PermissionError as e:
    print(e)

except FileNotFoundError:
    print("Error: File not found")

finally:
    print("Thank you for using Smart University Management System")