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
import pandas as pd
import seaborn as sns

# Veri setindeki tüm columnları göremiyorsanız : pd.set_option("display.max_columns", None)

# Dataframe oluşturmak için:
df = sns.load_dataset("titanic")
print(df.head())

# ... (burada "age") içerisinde var mı diye sormak için:
print("age" in df)

# Eğer içerisinde varsa "age" columnunu görmek için:
print(df["age"].head())

# Bu ifadenin type'ını görmek için:
print(type(df["age"].head())) # <class 'pandas.core.series.Series'> yani Series tipindedir. 

# Eğer dataframe olarak kalmasını istiyorsanız çift parantez kullanmalısınız.
print((df[["age"]]).head())
print(type((df[["age"]]).head())) # <class 'pandas.core.frame.DataFrame'> yani DataFrame tipindedir.
# Çift parantez kullanmamızın sebebi ortada bir liste olduğu için.

# Birden fazla column'u görmek için:
print(df[["age","alive"]].head())

# Index değeri olarak liste de kullanabiliriz.
col_names = ["age","adult_male","alive"]
print(df[col_names])

# Yeni bir column eklemek istersek (burada var olan column üzerinden:
df["age2"] = df["age"]**2
print(df.head())

# Oluşturduğumuz yeni columndan ('age2') ve 'age' den age3 columnını görmek için:
df["age3"] = df["age"] / df["age2"]

# Bakalım
print(df.head())

# Bir column'ı silmek için:
print(df.drop("age2", axis=1,).head()) # Kalıcı değil kalıcı olması için inplace=True yazılır

# Daha detaylı seçim yapmak için:
print(df.loc[:, ~df.columns.str.containes("age")].head()) # ~ ile kolonlarının içinde "age" yoksa alır. Eğer ~  yı kaldırırsak içinde "age" olanları alır. 

################################################################################
#Loc ve Iloc
################################################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
print(df.head())

# iloc: integer based selection
df.iloc[0:3]
print(df.iloc[0:3])
print(df.iloc[0,0])

# loc: label based selection
df.loc[0:3]
print(df.loc[0:3])

# iloc bizim bildiğimiz index mantığı ile veri setimizi seçerken loc bizim bildiğimiz label mantığı ile veri setimizi seçer.
# Yani değer ile seçme işlemi yapmak istersek loc kullanırız.
df.loc[0:3, "age"]
# Çalışırken df.iloc[0:3, "age"] çalışmaz. (integer değil)

# Yine fancy indexing kullanmak istersek loc kullanırız.
col_names = ["age","embarked","alive"]

################################################################################
#Koşullu Seçim
################################################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# Dataframelerin indexlerine kosullu ifade sorguları:
print(df[df["age"] > 50].head())
print(df[df["age"] > 50]["age"].count())

# Direkt değişkeni istersek eğer loc kullanmalıyız.
print(df.loc[df["age"] > 50, ["age","class"]].head())

# Birden fazla koşullu ifade kullanacaksak koşullar " (kosul) & (kosul) " şeklinde yazılmalıdır.
print(df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age","class"]].head())

# Daha fazla koşul gerekirse:
print(df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton"))
           , ["age","class","embark_town"]].head())


# Verilen dataframeden yeni dataframe yapmak:
df_new = df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton"))
           , ["age","class","embark_town"]]

# Dataframedeki embark_town değişkeninin sayılarına bakmak için:
print(df_new["embark_town"].value_counts())


############################################################################################
# Toplulaştırma ve Gruplama (Aggregation and Grouping)
############################################################################################

#count()
#first()
#last()
#mean()
#median()
#min()
#max()
#std()
#var()
#sum()
#pivot_table() haric hepsi group by ile yapılabilir.)

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
df["age"].mean()

# Cinsiyete göre yaş ortalamasını almak için.
df.groupby("sex")["age"].mean()

# Agg ile birden fazla metod uygulanabilir.
#df.groupby(["sex","embark_town"]).agg({"age": ["mean","sum",],"survived":["mean"]})
#df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum",],"survived":["mean"],"sex":["count"]})

################################################################################
#Pivot Table
################################################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# Pivot table verilerin gösterimini kolaylaştırır. Varsayılan olarak, verilen değerlerin ortalamasını alır.
df.pivot_table("survived","sex","embarked")

# Varsayılanı değiştirmek için "aggfunc" argümanı eklenir.
print(print(df.pivot_table("survived","sex","embarked",aggfunc="std"))) # Standart sapma hesaplandı.
# Pivot table aynı zaman da group by işlemide yapmış olur.

# İstersek farklı değişkenlere göre tekrar kırabiliriz. Örneğin:
print(df.pivot_table("survived","sex",["embarked","class"]))

# Dataframe'deki bir sayısal değişkeni kategorik değişkene çevirmek istersek 'pd.cut' veya 'pd.qcut' kullanılır.
# 'pd.cut' belirlediğimiz değer aralıklarına göre bölüp, kategorik değişken oluşturken 'pd.qcut' ise 
# çeyreklik (kartil) değerlerine göre kendi bölerek kategorik değişken oluşturur.

# Dataframe'de yeni yaş değişkeni oluşturalım.
df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])
df.head()
# Yeni yaş değişkeni ile pivot table yapalım.
print(df.pivot_table("survived","sex",["new_age","class"]))

################################################################################
# Apply ve Lambda
################################################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# Apply satır ve sütunlarda bir fonksiyon çalıştırma imkanı sağlar.
# Lambda kullan at fonksiyon kullanmayı sağlar.

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# Columnları üzerinde işlem yapıp görüntülemek için tek tek seçmemiz gerekir.
# Bunun önüne geçmek için döngü kullanılabilir.
for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10
print(df.head())

# Bir satıra bir fonksiyonu uygulamak için apply() kullanılır.
df[["age","age2","age3"]].apply(lambda x: x/10).head()

# İçerisinde 'age' isminde bir column varsa onu seçip apply uygulamak için:
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head())

# print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()) daha karışık hali

# Dışarıdan yazdığımız fonksiyonu da apply() fonksiyonunda kullanabiliriz.

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

print(df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head())
# df.loc[:,["age","age2","age3"]] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler)
df.loc[:,df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler)
print(df.head())

############################################################################################
# Birlestirme (Join) İşlemleri
############################################################################################
import numpy as np
import pandas as pd

m = np.random.randint(1,30,size=(5,3))

df1 = pd.DataFrame(m, columns=["var1","var2","var3"])
df2 = df1 + 99

# Birleştirme işlemi için pd.concat() kullanılır. Indexleri kopyalar. Yani index problemi oluşur
print(pd.concat([df1, df2]))

# Index problemini engellemek için ignore_index=True parametresi kullanılır.
print(pd.concat([df1, df2], ignore_index=True))

##############################################################################
#Merge İle Birleştirme İşlemi
##############################################################################

df1 = pd.DataFrame({'employees':['john','dennis','mark','maria'],
                    'group':['accounting','engineering','engineering','hr'],})

df2 = pd.DataFrame({'employees':['mark','john','dennis','maria'],
                    'start_date':[2010,2009,2014,2019]})

print(pd.merge(df1, df2))

# on parametresi hangi değişkenleri birleştirmek istiyorsak onu belirtiyoruz.
print(pd.merge(df1, df2, on='employees'))

# Amaç: Her çalışanın müdürünün bilgine erişmek
df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({'group':['accounting','engineering','hr'],
                    'manager':['Caner','Mustafa','Berkcan']})   # müdürler

print(pd.merge(df3, df4))
