# Custom context manager Write a class Timer usable as a context manager (with Timer():) that prints how long the block took to execute.    
from time import perf_counter

class Timer():
    def __init__(self):
        self.start = 0
        self.end = 0
    def __enter__(self):
        self.start = perf_counter()
        
    def __exit__(self, exc_type, exc, tb):
        self.end = perf_counter()
        print(f'{self.end - self.start} seconds')
        
        
    
    
    
def long_task():
    total = 0

    for i in range(100_000_000):
        total += i

    return total


with Timer():
    long_task()
