# Python Interview Exercises (30)

Grouped by difficulty. Try to solve each one without looking at `correction.md` first.
Write real code, run it, and check edge cases before peeking at the solution.

---

## 🟢 Beginner (1–10)

**1. FizzBuzz**
Print numbers from 1 to 100. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for multiples of both print "FizzBuzz".

**2. Reverse a string**
Write a function `reverse_string(s)` that returns the string reversed, without using `s[::-1]`.

**3. Palindrome check**
Write a function `is_palindrome(s)` that checks if a string is a palindrome (ignore case and spaces).

**4. Count vowels**
Write a function `count_vowels(s)` that returns the number of vowels in a string.

**5. Find the maximum**
Write a function `find_max(lst)` that returns the largest number in a list, without using `max()`.

**6. Sum of a list**
Write a function `sum_list(lst)` that returns the sum of all elements, without using `sum()`.

**7. Remove duplicates**
Write a function `remove_duplicates(lst)` that returns a list with duplicates removed, preserving order.

**8. FizzBuzz with a twist — counting**
Write a function `count_multiples(lst, n)` that returns how many numbers in `lst` are divisible by `n`.

**9. Temperature converter**
Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.

**10. Simple calculator**
Write a function `calculate(a, b, op)` where `op` is one of `"+"`, `"-"`, `"*"`, `"/"`, returning the result. Handle division by zero gracefully.

---

## 🟡 Intermediate (11–20)

**11. Anagram check**
Write a function `is_anagram(s1, s2)` that returns `True` if two strings are anagrams of each other.

**12. Word frequency**
Write a function `word_frequency(text)` that returns a dictionary mapping each word to its number of occurrences.

**13. Flatten a nested list**
Write a function `flatten(lst)` that flattens an arbitrarily nested list, e.g. `[1, [2, [3, 4], 5]] -> [1, 2, 3, 4, 5]`.

**14. FizzBuzz using list comprehension**
Rewrite exercise 1 as a one-line list comprehension that returns a list of strings/numbers instead of printing.

**15. Second largest element**
Write a function `second_largest(lst)` that returns the second largest unique value in a list.

**16. Group anagrams**
Write a function `group_anagrams(words)` that groups a list of words into lists of anagrams.

**17. Custom `zip`**
Implement your own version of `zip()` called `my_zip(*iterables)` using a generator.

**18. Matrix transpose**
Write a function `transpose(matrix)` that transposes a 2D list (list of lists), without using `numpy`.

**19. Two Sum**
Write a function `two_sum(nums, target)` that returns the indices of two numbers that add up to `target`, in O(n) time.

**20. Custom context manager**
Write a class `Timer` usable as a context manager (`with Timer():`) that prints how long the block took to execute.

---

## 🔴 Advanced (21–30)

**21. Decorator for timing**
Write a decorator `@timeit` that prints how long a function took to run, and returns the original result.

**22. Decorator with arguments**
Write a decorator `@retry(n)` that retries a function up to `n` times if it raises an exception, then re-raises.

**23. Custom iterator**
Write a class `Fibonacci` that is iterable and yields Fibonacci numbers up to `n` terms, implementing `__iter__` and `__next__`.

**24. LRU cache from scratch**
Implement a simple `LRUCache` class (without `functools.lru_cache`) supporting `get(key)` and `put(key, value)` with a fixed capacity.

**25. Merge intervals**
Write a function `merge_intervals(intervals)` that merges all overlapping intervals, e.g. `[[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]`.

**26. Deep copy without `copy` module**
Write a function `deep_copy(obj)` that recursively deep-copies a nested structure of lists/dicts, without using the `copy` module.

**27. Thread-safe counter**
Write a class `Counter` with an `increment()` method that is safe to call from multiple threads simultaneously (using `threading`).

**28. Generator-based pipeline**
Write three generator functions `read_numbers(lst)`, `square(gen)`, and `filter_even(gen)` and chain them to process a list lazily.

**29. Metaclass singleton**
Implement the Singleton pattern using a metaclass, so any class using it only ever has one instance.

**30. Async fetch simulation**
Using `asyncio`, write an `async def fetch(id, delay)` function that simulates a network call (via `asyncio.sleep`) and a `main()` that runs several `fetch` calls concurrently with `asyncio.gather`, printing total time taken.

---

Good luck! When you're ready, compare your solutions with `correction.md`
