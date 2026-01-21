class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display_details(self):
        print(self.name)
        print(self.rollno)

S1=Student("Ram",1)
S1.display_details()
S2=Student("Laxman",2)
S2.display_details()