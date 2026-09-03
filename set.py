# BLOCK 7 — SET
# Set unique values store karta hai.
number ={1,2,22,2,2,4,3,5}
print(number)
# A | B    # union
# A & B    # intersection
# A - B    # difference
a1 = {1,2,100,3,4,2,5,6,7,8}
b = [3,22,33,4,5,6,7,8,9]
# print(a | b)
# print(a & b)
# print(a - b)
# list me se duplicate remove kro
a = set(b)
print(a)
# Q21. Check karo ek set doosre ka subset hai ya nahi
# issubset is a method
ab = {1,2,3,4}
ba = {2,3,4,5,6,7,7,1,4}
print(ab.issubset(ba))

