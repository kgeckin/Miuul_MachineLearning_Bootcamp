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

#####################################################################
# 5 - Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan 
#     bu listeleri return eden fonksiyon yazınız.
#####################################################################
l = [2, 13, 18, 93, 22]

def oddEven(myList):
    #output = [[], []]
    odd = []
    even = []
    for i in myList:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

even, odd = oddEven(l)


###############################################
# 6 - List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

# Beklenen Çıktı

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.head()
df.columns
df.info()
df["total"].dtype


["NUM_" + i.upper() if df[i].dtype != "O" else i.upper() for i in df.columns]


# [ ifYapılacak if condition else elseYapılacak  for]





###############################################
# 7 - List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
###############################################

# Notlar:
# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.

# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

# [ ifYapılacak if else elseYapılacak  for]


import seaborn as sns
df = sns.load_dataset("car_crashes")


[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


###############################################
# 8 - List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
###############################################

# og_list = ["abbrev", "no_previous"]

# Notlar:
# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# Beklenen çıktı:

#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630


og_list = ["abbrev", "no_previous"]


import seaborn as sns
df = sns.load_dataset("car_crashes")

df.head()
df.columns

new_cols = [col for col in df.columns if col not in og_list]
df[new_cols].head()
