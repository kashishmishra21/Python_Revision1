# Python me mainly 2 types ke loops hote hain:
# for loop
# while loop
# for i in range(5):
#     print(f"hello world : {i}")

#  FOR LOOP
# for loop ka use tab karte hain jab hume pata ho ki kitni baar loop chalana hai ya kisi sequence/list/string ke har element par kaam karna hai.
# range() ko properly samjho
# range() loops me bahut important hai.
# range(start, stop)

# for i in range(2,10):
#     print(f"hello : {i}")
# start included hota hai, stop excluded hota hai.

# # range(start, stop, step)
# for i in range(100,10,-1):
#     print(f"kashish {i}") # kashish 1
# kashish 3
# kashish 5
# kashish 7
# kashish 9
#  print number 10 down to 1 using while loop 
i= 2
# while (i>=1):
#     i-=1
#     print(f"kashish {i}")
#  print all even numver between 1 - 50 using while loop
while i<=50:
    if i % 2 == 0:
        print(i)
    i+=2
# write a program sum of n natural no n =  5 => 15
n = int(input("Enter number:- "))
sum = 0
while n >= 1:
    sum = sum + n
    n = n - 1
print(sum)

   





















