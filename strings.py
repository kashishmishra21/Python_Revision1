#strings in python :- stores data in sequence of characters -- enclosed in ('',"",''' ''')
# strings are inmutuable , cant be changed once created 
str1 = "kashish"
str2 = 'kashish'
str3 = ''' kashihsh ''' # teeno sahi tareeke hai 
# string concatination
print("hello" + "   mishra")
# length of string len function 
str  = "kashishmisgra"
print(len(str))
# slicing 
str = "gulab jamun"
firsthalf = str[0:5] # gulab 
print(firsthalf)

# take input and print middle 3 values , and last 2 charater
hello = "Kashish6mishra"
mid = len(hello)//2 # 7
output = hello[mid-1 : mid+3] # 7-1 : 7+3 == h6mi
print(output)
output2 = hello[-2:]
print(output2)





