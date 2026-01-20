from abc import ABC,abstractmethod
class CLASS(ABC):
    @abstractmethod
    def subs(self):
        pass
    @abstractmethod
    def marks(self):
        pass

class SCHOOL(CLASS):
    def subs(self):
        print("Subs based on class")
    def marks(self):
        print("marks based on student")

s=SCHOOL()
s.subs()
s.marks()