a=[1,2,3,4,5,6,7,8,9,0]
b=["vikky","wipro","techademy","2026"]
list=[1,"vikky",2,"wipro",3,"techademy",4,"2026"]
print(a)
print(b)
print(list)
print(list[1])
for i in a:
    print(i)
for i in b:
    print(i)
for i in list:
    print(i)


if "vikky" in a:
    print("found")

list.reverse()
print(list)

list.append('2')
print(list)
list.remove("wipro")
print(list)
list.insert(3,"4")
print(list)