# largest no find 
# n1 = int(input(" "))
# n2 = int(input(" "))
# n3 = int(input(" "))
# if n1 > n2 and n1 > n3:
#     print("n1 is greater")
# elif n2 > n1 and n2 > n3:
#     print("n2 is greater")
# elif n3 > n2 and n3 > n1:
#     print("n3 is greater")
# elif(n1 == n2 and n2 == n3 and n3 == n1):
#     print("equal")
# else:
#     print("small")

# text.upper()
# text.lower()
# text.capitalize()
# text.title()
# text.strip()
# text.replace()
# text.split()
hello = "    kasish mishra hai"

print(hello.upper())
print(hello.lower())
print(hello.capitalize())
print(hello.title())
print(hello.strip())
print(hello.replace("kasish","hellohi"))
aa = "knjal kinjal kinjal kinjal kinjal"
print(aa.replace("kinjal","abhay",2))
print(hello.split())

words = ["kinjal","hello" , "komall" ,"poonam"]
print("::".join(words))
print(aa.find("komal"))
print(aa.index("kinjal"))
print(aa.count("l"))
text = "hello i am kasish mishra"
print(text.startswith("hello"))
print(text.endswith("mishra"))

number = "1234553432hkkk"
number2 = "kashish"
print(number.isdigit())
print(number2.isalpha())
print(number.isalnum())
abc = "KASHISH mishra"
print(abc.swapcase())
print(abc.center(90))
print(abc.ljust(20,"-"))
print(abc.rjust(90,"*"))
no = "1234"
# kisi k age  zeroo add krna hai , kitne no. cahiye bta doo or bracket me likh do or us hisab se age zero add ho jyege
print(no.zfill(9))
print(no.rev())
