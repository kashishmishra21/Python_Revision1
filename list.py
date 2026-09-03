# # List ka use multiple values ko ek hi variable mein store karne ke liye hota hai.
# fruits = ["apple","banana","pineapple","orange","mango"]

# print(fruits[0])
# print(fruits[-3])
# fruits[2] = "kashish21"
# fruits.append("looki")
# # agar kisi specific position pr value insert krni ho to hum insert ka use krte hai or usme value or index do parameter hote hai 
# fruits.insert(2,"kashish")
# fruits.extend(["lkkihjd","poookijh"])
# fruits.append(["kinjal123","jinjali765"])
# # output:-
# # ['apple', 'banana', 'kashish', 'kashish21', 'orange', 'mango', 'looki', 'lkkihjd', 'poookijh', ['kinjal123', 'jinjali765']]

# # append vs extend()
# # append me jb hum elemnts ko [] k sth add krenge too ek set me add hoga mtlb list k andar list bnti hai or extend me aysa nhi hota usme list k andar elements add ho jate hai 
# print(fruits)
# # 9. pop()
# # pop() index ke basis par element remove karta hai.
# print(fruits.pop(2))
# print(fruits.clear())
# hel = ["looki","poonam","pokkka","uijkuy"]
# print("looki" in hel)
# print("poonam" not in hel)
# cou = [100,222,782,842,2,2,2,2,2,3,4,5,5,5,6]
# cou.sort()
# print(cou)
# print(cou.count(2))
# cou.reverse()
# print(cou)
# print(cou[::2])
# print(cou*2)


# Methods in list
# food = ["samosa","pizza","toffee","burger","lolipop"]
marks = [99,98,78,65,55,21,22]
# marks[2] = 1000
# print(marks)
# name = "kashish mishra"
# marks[1]= "z"
# print(marks)

print(min(marks))
print(max(marks))
marks.sort()
print(marks)
print(marks.pop(3))
marks.insert(2,100001)
print(marks)






