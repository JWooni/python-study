a = [1,2,3,4]
b = a[:]
print(a == b)
print(a is b)

print(id(a))
print(id(b))

print(a[1] == b[1])
print(a[1] is b[1])

print(id(a[1]))
print(id(b[1]))

print(id(a[1]))
print(id(b[1]))

print(a[1])
print(b[1])