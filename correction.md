# Corrections — Python Interview Exercises

Reference solutions. There's often more than one valid approach — if yours differs but works and is reasonably clean, that's fine.

---

## 🟢 Beginner

**1. FizzBuzz**
```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**2. Reverse a string**
```python
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result
```

**3. Palindrome check**
```python
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
```

**4. Count vowels**
```python
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
```

**5. Find the maximum**
```python
def find_max(lst):
    if not lst:
        raise ValueError("empty list")
    current_max = lst[0]
    for x in lst[1:]:
        if x > current_max:
            current_max = x
    return current_max
```

**6. Sum of a list**
```python
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total
```

**7. Remove duplicates**
```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
```

**8. Count multiples**
```python
def count_multiples(lst, n):
    return sum(1 for x in lst if x % n == 0)
```

**9. Temperature converter**
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
```

**10. Simple calculator**
```python
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")
```

---

## 🟡 Intermediate

**11. Anagram check**
```python
def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)
```

**12. Word frequency**
```python
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        w = w.strip(".,!?;:")
        freq[w] = freq.get(w, 0) + 1
    return freq
```

**13. Flatten a nested list**
```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

**14. FizzBuzz with list comprehension**
```python
def fizzbuzz_list(n=100):
    return [
        "FizzBuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i
        for i in range(1, n + 1)
    ]
```

**15. Second largest element**
```python
def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    if len(unique) < 2:
        raise ValueError("need at least 2 unique values")
    return unique[1]
```

**16. Group anagrams**
```python
def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

**17. Custom `zip`**
```python
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        result = []
        for it in iterators:
            try:
                result.append(next(it))
            except StopIteration:
                return
        yield tuple(result)
```

**18. Matrix transpose**
```python
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
```

**19. Two Sum**
```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return None
```

**20. Custom context manager**
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False  # don't suppress exceptions
```

---

## 🔴 Advanced

**21. Decorator for timing**
```python
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
```

**22. Decorator with arguments**
```python
from functools import wraps

def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt} failed: {e}")
            raise last_exc
        return wrapper
    return decorator
```

**23. Custom iterator**
```python
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.a, self.b = 0, 1
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value
```

**24. LRU cache from scratch**
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

**25. Merge intervals**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged
```

**26. Deep copy without `copy` module**
```python
def deep_copy(obj):
    if isinstance(obj, dict):
        return {k: deep_copy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [deep_copy(v) for v in obj]
    elif isinstance(obj, tuple):
        return tuple(deep_copy(v) for v in obj)
    else:
        return obj  # immutable / primitive, safe to share
```

**27. Thread-safe counter**
```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1
```

**28. Generator-based pipeline**
```python
def read_numbers(lst):
    for n in lst:
        yield n

def square(gen):
    for n in gen:
        yield n * n

def filter_even(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

# Usage:
# pipeline = filter_even(square(read_numbers([1, 2, 3, 4, 5])))
# list(pipeline) -> [4, 16]
```

**29. Metaclass singleton**
```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

# Database() is Database()  -> True
```

**30. Async fetch simulation**
```python
import asyncio
import time

async def fetch(id, delay):
    print(f"Fetching {id}...")
    await asyncio.sleep(delay)
    print(f"Done {id}")
    return f"result-{id}"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch(1, 2),
        fetch(2, 1),
        fetch(3, 3),
    )
    elapsed = time.perf_counter() - start
    print(f"All done in {elapsed:.2f}s, results: {results}")

# asyncio.run(main())
```