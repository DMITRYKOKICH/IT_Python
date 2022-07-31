def my_func1(a):
    pass


def my_func2(c=1):
    print(c)

q=my_func2()


def my_fun3c(b):
    print(b)


def my_func4(*args):
    print(args)


my_func4(1,2,3,4)

def my_func5(**кwargs):
    print(кwargs)

my_func5 (a=1, b=2, c=3)

def my_func6 (*args, **кwargs):
    print(args,кwargs)

my_func6(1, 2, 3, 'abc', a=1, b=2, c=3)






a= [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]

for i in a :
    if i < 5:
        print(i)


my_list= ["msk", "spb", "nalchik"]
for i in my_list:

    print(i)

my_dict= {'k': 1, 'v': 2, 'c': 3}
for k, v in my_dict.items():
    print(k,v)

def my_func10(t):
    if t >5:
        print(t)

t = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]

l1= [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
l2= [1, 2, 1, 2, 101, 7, 43, 9, 10, -1, 0]



a = [1,2,3]

i = 0
while i < len(a):
    print(a[i])
    i = i + 1


def my_func7(e, r):
    j = 0
    while j < len(e):
        for y in r:
            if y == e[j]:
                e.remove(y)
        j = j + 1
    print(e)

my_func7(l1, l2)









def my_func11(my_dict):
    for k, v in my_dict.items():
        print(k)
        print(v)


my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

my_func11(my_dict)



