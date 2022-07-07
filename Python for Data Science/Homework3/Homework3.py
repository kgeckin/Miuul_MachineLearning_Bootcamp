#####################################################################
#1
#####################################################################
x = 8
print(type(x))

y = 3.2
print(type(y))

z = 8j + 18
print(type(z))

a = "Hello World"
print(type(a))

b = True
print(type(b))

c = 23 < 22
print(type(c))

l = [1,2,3,4]
print(type(l))

d = {"Name": "Jake",
     "Age":27,
     "Adress": "Downtown"
     }
print(type(d))

t = {"Machine Learning","Data Science"}
print(type(t))

s = {"Python","Machine Learning","Data Science"}
print(type(s))

#####################################################################
#2
#####################################################################
"""
Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız.
"""

text = "The goal is to turn data into information, and information into insight."
u = text.upper()
print(u.split(" "))

