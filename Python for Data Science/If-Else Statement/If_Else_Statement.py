
# KOŞULLAR (CONDITIONS)

if 1 == 1:
    print("Something")

if 1 == 2:
    print("Something")


def number_check(number):
    if number == 10:
        print("Number is 10")

number_check(12)
number_check(10)

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)

##########################################################################################################################
# DÖNGÜLER (LOOPS)
##########################################################################################################################

students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary* 20 / 100 + salary))

def newSalary(salary, rate):
    return int(salary * rate / 100 + salary)

print(newSalary(1500,10))
print(newSalary(2000,20))

for salary in salaries:
    print(newSalary(salary, 20))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(newSalary(salary, 15))

for salary in salaries:
    if salary > 3000:
        print(newSalary(salary, 10))
    else:
        print(newSalary(salary, 20))

# iki değer arasında sayı üretmeyi sağlamak:
print(range(0,5))
for i in range(0,5):
    print(i)
############################################################################################################################

# Mülakat Sorusu
# Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
def alternating(string):
    newString = ""
    for stringIndex in range(len(string)):
        if stringIndex % 2 == 0:
            newString += string[stringIndex].upper()
        else:
            newString += string[stringIndex].lower()
    print(newString)

alternating("hi my name is john and i am learning python")
# Sonuç önce = "hi my name is john and i am learning python"
# Sonuç sonra =  "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

#############################################################################################################################

# Break döngüyü bitirir.
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

#continue döngüye devam eder.
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while

number = 1
while number < 5:
    print(number)
    number += 1
    
###############################################################################################################################
# Enumerate: Otomatik Counter/Indexer ile for loop


students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []
for index,student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(A)
print(B)

#Uygulama - Mülakat sorusu

"""
divide_students fonksiyonu yazınız.
Çift indexte yer alan öğrencileri bir listeye alınız.
Tek indexte yer alan öğrencileri başka bir listeye alınız.
Fakat bu iki liste tek bir liste olarak return olsun.
"""
students = ["John", "Mark", "Venessa", "Mariam"]
def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
divide_students(students)

def alternatingWithEnumarate(string):
    newString = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            newString += letter.upper()
        else:
            newString += letter.lower()
    print(newString)
alternatingWithEnumarate("hi my name is john and i am learning python")

###########################################################################################################################
"""
lambda : Fonksiyonu tek satırda yazma
lambda parameters : yapılacak işlemler

"""

summer = lambda a,b : a + b
print(summer(2,3))

# map : bir fonksiyona bir datanın elemanlarını sırasıyla gönderir ve sonucu tek obje olarak döndürür
salaries = [1000, 2000, 3000, 4000, 5000]

def newSalary(x):
    return x * 20 / 100 + x

newSalary(5000)

for salary in salaries:
    print(newSalary(salary))

print(list(map(newSalary, salaries)))

# del newSum
print(list(map(lambda x: x * 20 / 100 + x, salaries)))
print(list(map(lambda x: x ** 2 , salaries)))

# Filter
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_store)))

# Reduce : döngüdede olabilecek veri tipinde elemanları azaltır ve karşılaştırma yaptırır.
from functools import reduce
list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store))

# zip : gruplama yaptırır

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

print(list(zip(students, departments, ages)))
