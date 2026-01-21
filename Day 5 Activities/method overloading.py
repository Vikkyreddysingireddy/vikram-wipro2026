class box1:
    def __init__(self, value):
        self.value = value
    def add(self,other):
        return self.value + other.value
    def __add__(self, other):
        return self.value + other.value


b1 = box1(50)
b2 = box1(30)
#1st method using dunder function
print(b1+b2)
#2nd method using method calling
print(b1.add(b2))