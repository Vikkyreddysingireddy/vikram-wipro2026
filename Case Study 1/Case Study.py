from abc import ABC, abstractmethod
from functools import wraps
import csv
import json
import os

def admin_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.current_role != "admin":
            print("Access Denied: Admin privileges required")
            return
        return func(self, *args, **kwargs)
    return wrapper

class MarksDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        setattr(instance, self.private_name, value)

class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Invalid salary")
        instance._salary = value

class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def get_details(self):
        avg, grade = self.calculate_performance()
        print("--------------------------------")
        print(f"ID        : {self.pid}")
        print(f"Name      : {self.name}")
        print(f"Department: {self.department}")
        print(f"Semester  : {self.semester}")
        print(f"Average   : {avg}")
        print(f"Grade     : {grade}")

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("--------------------------------")
        print(f"ID        : {self.pid}")
        print(f"Name      : {self.name}")
        print(f"Department: {self.department}")

class Course:
    def __init__(self, code, name, credits, faculty_id):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty_id = faculty_id
        self.students = []

    def enroll(self, student):
        self.students.append(student)

class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.current_role = None
        self.load_students_from_files()
        self.load_faculty_from_files()
        self.load_courses_from_files()

    def load_students_from_files(self):
        if os.path.isfile("studentsdata.json"):
            with open("studentsdata.json", "r") as f:
                data = json.load(f)
            for s in data:
                self.students[s["id"]] = Student(
                    s["id"], s["name"], s["department"],
                    s["semester"], s["marks"]
                )

    def load_faculty_from_files(self):
        if os.path.isfile("facultydata.json"):
            with open("facultydata.json", "r") as f:
                data = json.load(f)
            for fdata in data:
                self.faculty[fdata["id"]] = Faculty(
                    fdata["id"], fdata["name"],
                    fdata["department"], fdata["salary"]
                )

    def load_courses_from_files(self):
        if os.path.isfile("coursedata.json"):
            with open("coursedata.json", "r") as f:
                data = json.load(f)
            for c in data:
                self.courses[c["code"]] = Course(
                    c["code"], c["name"],
                    c["credits"], c["faculty_id"]
                )

    def login(self):
        role = input("Enter role (admin/user): ").lower()
        if role not in ("admin", "user"):
            raise ValueError("Invalid role")
        self.current_role = role
        print(f"Logged in as {role.upper()}")

    def save_student_files(self, s):
        data = []
        if os.path.isfile("studentsdata.json"):
            with open("studentsdata.json", "r") as f:
                data = json.load(f)
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
        with open("studentsdata.json", "w") as f:
            json.dump(data, f, indent=4)

        exists = os.path.isfile("studentsdata.csv")
        with open("studentsdata.csv", "a", newline="") as f:
            w = csv.writer(f)
            if not exists:
                w.writerow(["ID", "Name", "Department", "Semester", "Marks"])
            w.writerow([s.pid, s.name, s.department, s.semester, " ".join(map(str, s.marks))])

    def save_faculty_files(self, f):
        data = []
        if os.path.isfile("facultydata.json"):
            with open("facultydata.json", "r") as fh:
                data = json.load(fh)
        data.append({
            "id": f.pid,
            "name": f.name,
            "department": f.department,
            "salary": f._salary
        })
        with open("facultydata.json", "w") as fh:
            json.dump(data, fh, indent=4)

        exists = os.path.isfile("facultydata.csv")
        with open("facultydata.csv", "a", newline="") as fh:
            w = csv.writer(fh)
            if not exists:
                w.writerow(["ID", "Name", "Department", "Salary"])
            w.writerow([f.pid, f.name, f.department, f._salary])

    def save_course_files(self, c):
        data = []
        if os.path.isfile("coursedata.json"):
            with open("coursedata.json", "r") as f:
                data = json.load(f)
        data.append({
            "code": c.code,
            "name": c.name,
            "credits": c.credits,
            "faculty_id": c.faculty_id
        })
        with open("coursedata.json", "w") as f:
            json.dump(data, f, indent=4)

        exists = os.path.isfile("coursedata.csv")
        with open("coursedata.csv", "a", newline="") as f:
            w = csv.writer(f)
            if not exists:
                w.writerow(["Code", "Name", "Credits", "Faculty ID"])
            w.writerow([c.code, c.name, c.credits, c.faculty_id])

    @admin_required
    def add_student(self):
        sid = input("Student ID: ")
        if sid in self.students:
            raise ValueError("Student ID already exists")
        s = Student(
            sid,
            input("Name: "),
            input("Department: "),
            int(input("Semester: ")),
            list(map(int, input("Marks (5 subjects): ").split()))
        )
        self.students[sid] = s
        self.save_student_files(s)
        print("Student Created Successfully")

    @admin_required
    def edit_student(self):
        sid = input("Student ID to edit: ")
        s = self.students[sid]
        s.name = input("New Name: ")
        s.department = input("New Department: ")
        s.semester = int(input("New Semester: "))
        s.marks = list(map(int, input("New Marks: ").split()))
        print("Student details updated successfully")

    @admin_required
    def add_faculty(self):
        fid = input("Faculty ID: ")
        f = Faculty(
            fid,
            input("Name: "),
            input("Department: "),
            int(input("Salary: "))
        )
        self.faculty[fid] = f
        self.save_faculty_files(f)
        print("Faculty Created Successfully")

    @admin_required
    def edit_faculty(self):
        fid = input("Faculty ID to edit: ")
        f = self.faculty[fid]
        f.name = input("New Name: ")
        f.department = input("New Department: ")
        f.salary = int(input("New Salary: "))
        print("Faculty details updated successfully")

    @admin_required
    def add_course(self):
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fid = input("Faculty ID: ")
        c = Course(code, name, credits, fid)
        self.courses[code] = c
        self.save_course_files(c)
        print("Course Added Successfully")

    @admin_required
    def compare_students(self):
        s1 = self.students[input("First Student ID: ")]
        s2 = self.students[input("Second Student ID: ")]
        print(f"{s1.name} > {s2.name} :", s1 > s2)

    def view_student_details(self):
        self.students[input("Student ID: ")].get_details()

    def view_faculty_details(self):
        self.faculty[input("Faculty ID: ")].get_details()

    def enroll_student(self):
        sid = input("Student ID: ")
        code = input("Course Code: ")
        self.courses[code].enroll(self.students[sid])
        print("Enrollment Successful")

    def calculate_performance(self):
        sid = input("Student ID: ")
        avg, grade = self.students[sid].calculate_performance()
        print(f"Average: {avg}, Grade: {grade}")

    def menu(self):
        while True:
            try:
                if self.current_role == "admin":
                    print("""
ADMIN MENU
--------------------
1. Add Student
2. Edit Student
3. Add Faculty
4. Edit Faculty
5. Add Course
6. Compare Students
7. Exit
""")
                    ch = input("Enter choice: ")
                    if ch == "1": self.add_student()
                    elif ch == "2": self.edit_student()
                    elif ch == "3": self.add_faculty()
                    elif ch == "4": self.edit_faculty()
                    elif ch == "5": self.add_course()
                    elif ch == "6": self.compare_students()
                    elif ch == "7": break
                    else: print("Invalid choice")
                else:
                    print("""
USER MENU
--------------------
1. View Student Details
2. View Faculty Details
3. Enroll Student
4. Exit
""")
                    ch = input("Enter choice: ")
                    if ch == "1": self.view_student_details()
                    elif ch == "2": self.view_faculty_details()
                    elif ch == "3": self.enroll_student()
                    elif ch == "4": break
                    else: print("Invalid choice")
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    system = UniversitySystem()
    system.login()
    system.menu()
    print("Thank you for using Smart University Management System")
