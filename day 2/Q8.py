a=[1, 2, 3, 4, 5, 6, 2, 4]
b=map(lambda x:x**3,a)
c=dict(zip(a,b))
print(c)