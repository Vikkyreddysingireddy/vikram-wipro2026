A,B,C=1,2,3
if(A>B and B>C):
    print(A, "is greater than B and C")
elif(B>C and B>A):
    print(B, "is greater than A and C")
else:
    print(C, "is greater than A and B")



for i in range(0,21):
    print(i)



for i in range(0,21):
    if(i%2==0):
        print(i, "is an even number")
    else:
        print(i, "is an odd number")


i=10
while i!=0:
    print(i)
    i-=1

num=int(input("Enter a number: "))
match num:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case _:
        print("Invalid input")