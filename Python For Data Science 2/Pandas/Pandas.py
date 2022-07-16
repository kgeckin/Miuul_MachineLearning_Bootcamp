#################################################
#Pandas
#################################################
#Veri manipülasyonu için akıla gelen ilk kütüphanedir.
#Ekonometrik ve finansal çalışmalar için doğmuş.
#2008 yılında temeli atılmıştır.

#İçindekiler
    # Pandas series
    # Veri okuma
    # Veriye hızlı bakış
    # Pandas'ta seçim işlemleri
    # Topluluklaştırma ve gruplama
    # Apply and lambda
    # Birleştırme işlemleri

#############################################################
#Pandas Series
#############################################################

#Serileri : Tek boyutlu ve index bilgisi bulunduran veri tipi
#DataFrame : Çok boyutlu ve index bilgisi bulunduran veri tipi

import pandas as pd
s = pd.Series([10,77,12,4,5]) #method. Verilen listeyi pandas verisine döndürür.
type(s) #pandas.core.series.Series
s.index #RangeIndex(start=0, stop=5, step=1)
s.dtype #tip bilgisini verir. dtype('int64')
s.size # 5 elemanlı
s.ndim #boyut bilgisi : 1
#Pandas serileri tek boyutludur.
s.values #değerlere erişmek için. serilerle ilgili metodlarda uygulanmaz.
type(s.values) #numpy.ndarray
s.head(3) #ilk 3'ü değeri getirdi
s.tail(3) #son 3'ü değeri getirdi


#############################################################
#  Veri Okuma
#############################################################

#csv,txt,excell okuyabilir.

df = pd.read_csv("datasets/coronavirus.csv")
df.head()

#pd üzerine gelip ctrl dersek help menüsü açılır.

#############################################################
# Veriye Hızlı Bakış
#############################################################
import pandas as pdf
import seaborn  as sns

df = sns.load_dataset("titanic") #seaborn load_dataset ile veri setlerine erişebiliriz.
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T #Transpozesini alıyor.
df.isnull().values.any() #eksik değer var mı?
df.isnull().sum() #eksiklerin değişkenlerde ne kadar olduğunu belirtir.
df["sex"].head() #kategori içerisindeki değerlere ulaşma
df["sex"].value_counts() #kategori içerisinde kaç tane ne var açıklar

##############################################################
#Pandas Seçim İşlemleri
#############################################################

import pandas as pdf
import seaborn  as sns

df = sns.load_dataset("titanic")
df.head()
df.index
df[0:13]
#drop metodu silmek için kullanılır. Yapısı (index, satır/sütun) ve görmek için head()
df.drop(0,axis=0).head()

#birden çok silmek için
deleted_index = [1,3,5,7]
df.drop(deleted_index, axis=0).head(10) #kalıcı değildir.
# Kalıcı olması için:
# df = df.drop(deleted_index, axis=0).head(10)
# df.drop(deleted_index, axis=0, inplace = True).head(10)
# inplace metodu ile değişkeni kalıcı hale getiririz.

############################################################
#Değişkeni Indexe Çevirme
############################################################
df["age"].head()
df.age.head()
df.index = df["age"] #indexe çevrilir.
#Index olarak aldığımız değişkeni drop metodu ile sileriz.
df.drop("age", axis = 1).head() #yaş değişkeni artık indexte mevcuttur.


############################################################
#Indexi Değişkene Çevirme
############################################################
#1.yol
df.index
df["age"] = df.index
df.head()
#2.yol
df.reset_index().head()
df = df.reset_index()
df.head()

###########################################################
#Değişkenler Üzerinde İşlemler
###########################################################

