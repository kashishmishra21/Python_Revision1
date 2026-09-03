# # BLOCK 7 — DICTIONARY
# # Dictionary data ko key : value pair mein store karti hai.
# # ex 
# student = {
#     "name" : "kashish",
#     "roll no" : 21,
#     "class" : "bca"
# }
# print(student["name"])
# print(student.get("roll no"))

# # 2. Value change karna
# student["roll no"] = 2200
# print(student.get("roll no")) # .get() se kch bhi get kr skte hai us dictionary k andar k data
# # 3. New item add karna   
# student["class"] = "management"
# print(student["class"])
# print(student)

# # 4. Item delete karna
# del student["roll no"]
# print(student)
# student.pop("class")
# print(student)


# # student.keys()
# # student.values()
# # student.items()
# # student.get("name")
# # student.pop("age")
# # student.update({"city": "Lucknow"})

# food = {
#     "fast" :"pizza",
#     "slow" : "roti",
#     "h": "abc",
#     "ahg" : "pio"
#     }
# if "fast" in food :
#     print("exist")
# else:
#     print("no exist")

# # Keys + Values dono print karna
# for key,value in food.items() :
#     print(f"{key} : {value}") 




# # print(food.keys())
# # print(food.values())
# # print(food.items())
# # food.update({"lko":"delhi"})
# # print(food)




# # list     → [1, 2, 3]
# # tuple    → (1, 2, 3)
# # set      → {1, 2, 3}
# # dict     → {"name": "Abhay", "age": 21}

# # Check karo dictionary mein "name" key exist karti hai ya nahi


# marks = {
#     "Rahul": 85,
#     "Priya": 92,
#     "Aman": 76,
#     "Neha": 89
# }

# for i in marks.values():
#     if i >= 80:
#         print("higher than usual")
#     else:
#         print("lower than 80") 

# # Q35: Isi dictionary se highest marks wale student ka naam find karo. 🔥

# high = 0
# topper = ""

# for name,value in marks.items():
#     if value > high:
#         high = value
#         topper = name

# print(f"{high}:{topper}")




student = {
    "name":"kashish",
    "age":21,
    "city":"lucknow"
}
print(type(student))
print(student.values())
student["age"] = 222
print(student)
student.pop("age")
print(student)

marks ={}
marks["Physics"]= 90
marks["chemistry"] = 900
marks["Science"] = 23
print(marks)

programing = ["python", "java", "c++", "python", "C", "java"]
programingset = set(programing)
print(type(programing))
print(type(programingset))
print(programingset)
print(len(programingset))
