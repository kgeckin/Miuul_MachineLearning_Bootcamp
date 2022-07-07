print("John")
print("John")

name = "X"

# Çok Satırlı Karakter Dizileri 

print(
    """
    Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool
    """
)

longStr = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""
print(longStr)

# Karakter Dizilerinin Elemanlarına Erişmek
# Python programlama dilinde index 0'dan başlar.
# İstenilen indexe erişimek için [] içerisinde yazılır.

print(name[0])
print(name[3])

# Karakter Dizilerinde Slice İşlemi 
# Belirlenen indexten istenen indexe kadar almayı sağlar.

print(name[0:2])
print(longStr[0:10])

# String içerisinde karakter sorgulama
# in operatörü ile yapılır.
# Büyük küçük harf duyarlıdır.

print("Veri" in longStr) #True
print("veri" in longStr) #Falce
print("bool" in longStr) 

# String Metotları

dir(str)

# len metodu 
# String değerin kaç elemandan oluştuğun verir.

print(len(name))
print(len("vahitkeskin"))
print(len("miuul"))

# upper() & lower()

print(name.upper())
print(name.lower())

# replace

hi = "Hello AI Era"
hi.replace("l", "p")
print(hi)

# split

print(hi.split()) #["Hello","AI","Era"]

# strip

print(" ofofo ".strip()) #ofofo
print("ofofo".strip("o")) #fof

# capitalize

print("foo".capitalize()) # Foo
