#####################################################################
# 1 - Verilen değerlerin veri yapılarını inceleyiniz.Type() metodunu kullanınız.
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
# 2 - Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
#####################################################################
text = "The goal is to turn data into information, and information into insight."
u = text.upper()
print(u.split(" "))

#####################################################################
# 3 - Verilen listeye aşağıdaki adımları uygulayınız.
#####################################################################
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# 1 - Verilen listenin eleman sayısına bakınız.
len(lst)

# 2 -Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# 3- Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
nw = lst[0:4]
print(nw)

# 4- Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
lst

# 5 - Yeni bir eleman ekleyiniz.
lst.append("W")
lst

# 6 - Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N")
lst

#####################################################################
# 4 - Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
#####################################################################

dict = {'Christian': ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# 1 - Key değerlerine erişiniz.
dict.keys()

# 2 - Value değerlerine erişiniz.
dict.values()

# 3 - Daisy keyine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13
dict

# 4 - Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
dict

# 5 - Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict
