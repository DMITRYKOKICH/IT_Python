import time

def deco(a):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        a(*args, **kwargs)
        end_time = time.time()
        res_time = end_time - start_time
        print("время выполнения:")
        print(res_time)
        return a
    return wrapper

@deco
def func(b):

    time.sleep(10)
    print("body of func")

@deco
def func2(c,d):
    print(c+d)
    print("body of func1234")

@deco
def func3(a):
    print(a)


func(3)
func(6)
func2 (12345, 987654)


t= time.time()
print(t)
