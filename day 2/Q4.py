from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
b=filter(lambda x:x%2==0,a)
c=map(lambda x:x**2,list(filter(lambda x:x%2==0,a)))
d=reduce(lambda x,y: x+y,c)
print(d)