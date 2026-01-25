class A:
    name="vikram"
    age=22
a=A()
print(a.name)
print(a.age)

class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
b=B("vikram",22)