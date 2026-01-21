from abc import ABC, abstractmethod


class Marks(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def total(self):
        pass


class Subject(Marks):
    def total(self):
        print(self.name, "Marks is 90")


m = Subject("English")
m.total()
