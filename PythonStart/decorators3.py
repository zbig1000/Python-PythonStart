### Initial Code

from time import time, sleep, time_ns

# Hint: call `time()` to get current time
# start = time()
# end = time()
# duration = end - start

def timeit(func):

    def wrapper(*args, **kwargs):
        start = time_ns()
        try:
            result = func(*args, **kwargs)
        finally:
            print("elapsed ", time_ns() - start)
        return result    

    return wrapper

### Expected behaviour
@timeit
def bar(a, b):
    sleep(0.1)
    retval = a / b
    sleep(0.1)
    return retval
print(bar(4, 2))
#Elapsed 0.208 sec
#2.0
# ★ Make sure it works even in case of an exception
print(bar(4, 1))
print(bar(4, 0))