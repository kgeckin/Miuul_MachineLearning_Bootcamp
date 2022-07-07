# List

# Değiştirilebilir
# Sıralıdır.
# Kapsayıcıdır.


notes = [1,2,3,4]
print(type(notes))
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
print(not_nam[0])
print(not_nam[5])
print(not_nam[6])
print(not_nam[6][1])

notes[0] = 99
print(notes)
print(not_nam[0:3])

# List Methods

# len() 
print(len(notes))
print(len(not_nam))

# append()
notes.append(100)
print(notes)

# pop()
notes.pop(1)
print(notes)

# insert(x,y)
notes.insert(2,5)
print(notes)
