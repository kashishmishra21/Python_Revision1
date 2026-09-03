#function.py
a = 2
b = 3
sum = a+b
print(sum)
# some more lines of code
# function is line of code which canrepeat multiple times in one go , we can define a function as def function_name and use that function multiple times
def greet():
    print("hello kashish Mishra")
greet()
greet()
def sum(a,b):
    return (a+b)
print(sum(8,9))
# write a function of square(num) that return a square of a number 
def square(num):
    return (num**2)
print(square(8))
# Write a function that takes a string and return the count of vowels and consonets separately
vowel = 'aeiouAEIOU'
userinput= input("Enter your name : ")
def count(userinput):
    countcons = 0
    countvow = 0 
    for char in userinput:
        if char.isalpha():
            if char in vowel:
                countvow += 1
            else:
                countcons += 1
    return countcons,countvow
countcons , countvow = count(userinput)
print(f"const :{countcons} vowel : {countvow}")

        


















