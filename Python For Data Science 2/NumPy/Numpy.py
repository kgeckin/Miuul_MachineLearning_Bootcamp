#####################################
# NumPy Array'i Oluşturmak
#####################################

import numpy as np

#En baştan array oluşturma
np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))

#Sıfırlardan array oluşturma
np.zeros(10, dtype=int)

#random int methodu ile array oluşturma
# 0-10 arasından 10 tane int üretildi
np.random.randint(0,10, size=10)

#belirli istatistik dağılım ile array
# ortalama, argüman, boyut bilgisi
np.random.normal(10,4,(3,4))

##########################################
# NumPy array özellikleri
##########################################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

#5 tane 0-10 arasında int
a=np.random.randint(10, size=5)
a.ndim #boyut sayısı 1
a.shape # boyut bilgisi (5,)
a.size # toplam eleman sayısı 5
a.dtype # array veri tipi dtype('int32')

################################################
#Yeniden şekillendirme
#############################################

#Boyut değiştirme
#rastgele sayılardan oluşmuş 1-10 arasında 9 tane int
np.random.randint(1,10,size=9)
np.random.randint(1,10,size=9).reshape(3,3)

#2. yontem
ar= np.random.randint(1,10,size=9)
ar.reshape(3,3)

##############################################
#Index İşlemleri
##############################################

a= np.random.randint(10,size=10)
a
a[0]
a[0:5]
a[0]=999

m=np.random.randint(10, size=(3,5))
m
m[0,0] #[satır,sütun]
m[2,3]=999
m[2,3]
m
#numpy sabit tipli array. Verimli veri saklar numpy. Tip bilgisi değişmez yani array içindeki diğer değerlere benzer değerler tanımlanacaktır.
m[:,0] #bütün satırları seç 0.sütunu seç demek.
m[1,:] #tüm sütunlardaki 1.satır
m[0:2,0:3] # satırda 0:2'ye sütunda 0:3'e kadar git demek.


#############################################
#Fancy Index
##############################################

v=np.arange(0,30,3) #0'dan 30'a kadar 3'erli array
v[1]
v[4]

#Fancy index ile erişmek istediğimiz elemanlara kısaca ulaşabiliyoruz
#Bunun için bir liste oluşturuyoruz ve bu listeyi np arrayde eleman çağırması yaparak çağırıyoruz.
catch=[1,2,3]
v[catch]

####################################################
#Numpy'da Koşullu İşlemler
####################################################

v = np.array([1,2,3,4,5])

#Klasik döngüyle erişmek
ab = []
for i in v:
    #print(i)
    if i < 3:
        ab.append(i)

#Numpy ile
v < 3
v[v < 3]

#########################################################
#Matematiksel İşlemler
#########################################################
v = np.array([1,2,3,4,5])
v / 5 # array([0.2, 0.4, 0.6, 0.8, 1. ])

#methodlar ile
np.subtract(v,1) #çıkartma
np.add(v,1) #toplama
np.mean(v) #ortalama
np.sum(v) #toplam alma
np.min(v) #
np.max(v) #
np.var(v) #varyans
#bunlar kalıcı değil atama yapılmalı
x = np.add(v,1)

##########################################
# İki bilinmeyenli denklem
##########################################

#5*x0+x1 =12
#x0+3*x1 =10

a = np.array([[5,1],[1,3]])
b = np.array([12,10])
c = np.linalg.solve(a,b)
