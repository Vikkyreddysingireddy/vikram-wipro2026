def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
print(add(1,2))
print(subtract(1,2))

def greetings(Greetings="Hi" ,name = "Vikram"):
    print("%s %s" %(Greetings,name))
greetings()
greetings("hello")
def pars(*params):
    print(params)
pars(1,2,3,4,5)
pars("s","u")

def valueparams(**params):
    print(params)
valueparams(a=1,b=2,c=3,d=4,e=5)