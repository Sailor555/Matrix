a = [1, 2, [3, 4]]
#b = a
b = list(a)
b[0] = 10
a.append(100)
b[2][0] = 30

print(a)
print(b)