
# 1
a = [1, 2, 3]
b = a

a = a + [4]

print(a)
print(b)
print(a is b)
#L'opération a + [4] crée une nouvelle liste, puis a est réaffecté à cette liste. 
# b référence toujours l'ancienne liste.
# 2
a = [1, 2, 3]
b = a

a += [4]

print(a)
print(b)
print(a is b)
#L'opération a += [4] modifie la liste existante en place, donc a et b font référence à la même liste.

