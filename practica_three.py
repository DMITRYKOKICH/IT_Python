add = lambda x, y: x + y
print(add(100, 200))

lambda x, y: x - y
print(add(1000, 99))

add =lambda x , y, a, b: (x + y) + (a + b)
print(add(1, 2, 3, 4))

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

l = [1, 2, 5, 3, 4]
l.sort(key=lambda x: x)
print(l)
