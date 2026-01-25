class classed:
    def __init__(self,name):
        self.name=name
        print("Contructor")

    def __del__(self):
        print("Destructor")

n= classed('n')