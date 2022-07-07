# Fonksiyon ne işe yarar?
# - Don't Repeat Yourself (DRY)


def selam():
    selam = "selamlar"
    print(selam)
    return selam

kelime = selam()
kelime

def seslen(kelime):
    return kelime

seslen("hey")

kelime = seslen("hey")
kelime


kelime = seslen("merhaba")

kelime

def seslen(kelime):
    print("kelimeyi kaydediyorum...")
    return kelime

kelime = seslen("Hey")
kelime


kelime*5

seslen("Hey") * 5
seslen("Hey").upper()


# Şimdiki yıl ve doğum yılı bilgilerini argüman olarak alan ve yaşı hesaplayan fonksiyonu yazınız.


def age(curr_year, birth_year):
    agee = curr_year - birth_year
    return agee

yas = age(2022, 2000)

yas * 5




def age(current_year, birth_year):
    print(current_year - birth_year)

age(2022, 2000)

age(1996, 2022)


# ön tanımlı argüman/parametre


def age(current_year=2022, birth_year= 2000):
    print(current_year - birth_year)

age()
age(2000, 1980)



# Fonksiyon İçerisinden Fonksiyon Çağırmak
def age(current_year=2022, birth_year= 1996):
    return current_year - birth_year


def sigorta(current_year, birth_year, Work_year):
    yas = age(current_year, birth_year)
    year = current_year - Work_year
    return yas * year

sigorta(2022, 2000, 2018)

"""
def age(current_year=2022, birth_year= 1996):
    print(current_year - birth_year)
    
Bu fonksiyon ile çağırsaydık çalışmazdı.
"""


# Docstring

def sum(arg1, arg2):
    """
    Sum of two numbers
    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    return arg1 + arg2

sayi = sum(3,5)
sayi


###############################################
# KOŞULLAR (CONDITIONS)
###############################################

def passed(mark):
    if mark == 60:
        print("sınırda geçtiniz")
        return "sınırda"+str(mark)
    elif mark > 60:
        print("geçtiniz")
        return "geçtin "+str(mark)
    else:
        print("kaldınız")
        return "kaldın"+str(mark)

passed(70)


exam_notes = [10,20,30,40,50,60,70]


for i in exam_notes:
    passed(i)

[passed(i) for i in exam_notes]


#######################
# break & continue & while
#######################
names = ["a", "b", "c", "d", "e"]


for name in names:
    if name == "c":
        break
    print(name)



for name in names:
    if name == "c":
        continue
    print(name)



# while


number = 1

while number < 20:
    print(number)
    #number += 1



# Enumerate: Otomatik Counter/Indexer ile for loop


names = ["ahmet", "mehmet", "saltuk", "cemal"]

for i, name in enumerate(names):
    print(i+1, name)




###############################################
# lambda
###############################################

def sum(a, b):
    return a + b

sum(1, 3)


new_sum = lambda a, b: a * b

new_sum(4, 5)


# map, filter, reduce

