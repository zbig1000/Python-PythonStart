#%%time

from concurrent import futures
from time import sleep, time

def foo():
    sleep(2.0)
    return 42

def bar():
    sleep(2.0)
    return 10
    
def task(delay):
    sleep(delay)
    return 42

start = time()

with futures.ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(bar)  
    future2 = pool.submit(foo)  
    print(future1.result() + future2.result())
end = time()

print(end-start)