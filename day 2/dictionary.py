marks={
    "physics" : 70,
    "chemistry" : 80,
    "mechanics" : 90,
    "english" : 90,
}
print(marks["physics"])
print(marks["chemistry"])
print(marks.get("mechanics"))
print(marks.get("english"))
print(marks.values())
print(marks.keys())
marks.pop("physics")
marks.popitem()
print(marks)

for key in marks:
    print(key, marks[key])
if "mechanics" in marks:
    print(marks["mechanics"])

cls={
    "Vivek" : {"maths": 15, "physics": 10, "chemistry": 10, "english": 10},
    "Abhi" : {"maths": 14, "physics": 23, "chemistry": 10, "english": 5},
    "Ram" : {"maths": 19, "physics": 6, "chemistry": 3, "english": 12}
}
print(cls)
print(cls["Ram"]["maths"])