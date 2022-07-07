# Dictionary(Sözlük)

# Değiştirilebilir.
# Sırasızdır. (3.7, sıralı olmuştur)
# Kapsayıcıdır.


dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}
print("REG")

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

print(dictionary["CART"])

# Key Sorgulama

print("YSA" in dictionary)

# Value Sorgulama


print(dictionary["REG"])
print(dictionary.get("REG"))

# Value Değiştirmek

dictionary["REG"] = ["YSA", 10]
print(dictionary)


# Tüm Keylere Erişmek

print(dictionary.keys())

# Tüm Valuelara Erişmek

print(dictionary.values())


# Tupple Yapmak

print(dictionary.items())

# Key-Value Değerini Güncellemek ve/veya Yeni Değerler Eklemek

dictionary.update({"REG": 11})

