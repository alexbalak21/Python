# Custom context manager Write a class Timer usable as a context manager (with Timer():) that prints how long the block took to execute.    

from contextlib import contextmanager
from time import perf_counter


@contextmanager
def Timer():
    start = perf_counter()
    yield
    end = perf_counter()
    print (f'{end-start} ms')
    
    
    
def long_task():
    total = 0

    for i in range(100_000_000):
        total += i

    return total


with Timer():
    long_task()
    