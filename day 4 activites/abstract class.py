from abc import ABC,abstractmethod

class shape(ABC):
    def display(self):
        print("display method")
    @abstractmethod
    def area(self):
        pass


class reactangle(shape):
    def area(self):
        print("rectangle method called")


r=reactangle()
r.area()
r.display()