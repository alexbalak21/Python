# Python Lists — 25 Exercises

Everything here is about `list`: indexing, slicing, comprehensions, mutation, sorting, and the classic interview traps.

---

## 🟢 Basics (1–8)

**1. Indexing & slicing**
Given `lst = [10, 20, 30, 40, 50, 60]`, write expressions that return:
the first element, the last element, the first three, the last two, every other element, and the list reversed.

**2. Build a list**
Write a function `first_n_squares(n)` returning `[1, 4, 9, ...]` for the first `n` integers.

**3. Insert and delete**
Write a function `insert_middle(lst, value)` that inserts `value` at the middle index of `lst` and returns the list.

**4. Count occurrences**
Write `count_occurrences(lst, x)` returning how many times `x` appears — without using `.count()`.

**5. Index of all matches**
Write `find_all(lst, x)` returning a list of every index where `x` appears.

**6. Swap two elements**
Write `swap(lst, i, j)` that swaps elements at positions `i` and `j` in place.

**7. Rotate a list**
Write `rotate(lst, k)` that rotates the list `k` positions to the right. `rotate([1,2,3,4,5], 2) -> [4,5,1,2,3]`.

**8. Chunk a list**
Write `chunks(lst, size)` returning a list of sublists of length `size` (last chunk may be shorter).

---

## 🟡 Comprehensions & transformations (9–17)

**9. Filter with a comprehension**
From a list of integers, build a list of only the even ones, squared.

**10. Nested comprehension**
Flatten `[[1,2],[3,4],[5,6]]` into `[1,2,3,4,5,6]` using a single comprehension.

**11. Conditional expression in a comprehension**
Given a list of numbers, produce a list where negatives are replaced by `0` and positives are kept.

**12. Pairs**
Given `a = [1,2,3]` and `b = ['x','y']`, build all pairs `[(1,'x'), (1,'y'), (2,'x'), ...]` with a comprehension.

**13. Zip two lists into a dict**
Given `keys` and `values` lists, build a dict mapping each key to its value.

**14. Enumerate**
Write `numbered(lst)` returning strings like `"0: apple"`, `"1: banana"`, ...

**15. Intersection and difference**
Write `intersection(a, b)` and `difference(a, b)` returning lists, preserving the order of `a`.

**16. Running total**
Write `cumulative(lst)` where `[1,2,3,4] -> [1,3,6,10]`.

**17. Interleave**
Write `interleave(a, b)` where `[1,2,3]` and `['a','b','c']` give `[1,'a',2,'b',3,'c']`. Handle lists of different lengths.

---

## 🔴 Sorting, mutation & traps (18–25)

**18. Sort by key**
Given `people = [("Alice", 30), ("Bob", 25), ("Eve", 35)]`, sort by age ascending, then by name descending.

**19. Sort strings by length then alphabetically**
Write `smart_sort(words)` sorting by length first, then alphabetically for ties.

**20. `sort()` vs `sorted()`**
Explain the difference, and show code proving that one mutates the original list and the other does not.

**21. The mutable default argument trap**
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```
What happens when you call `add_item(1)` then `add_item(2)`? Why? Fix it.

**22. The shallow copy trap**
```python
matrix = [[0] * 3] * 3
matrix[0][0] = 5
```
What is `matrix` now? Why? Build a 3×3 zero matrix correctly.

**23. Copy vs reference**
Show the difference between `b = a`, `b = a[:]`, and `b = copy.deepcopy(a)` when `a` is a list of lists.

**24. Removing while iterating**
```python
lst = [1, 2, 3, 4, 5, 6]
for x in lst:
    if x % 2 == 0:
        lst.remove(x)
```
What is the result, and why is it wrong? Give two correct ways to remove all even numbers.

**25. Performance**
Explain why `lst.insert(0, x)` and `lst.pop(0)` are O(n) while `lst.append(x)` and `lst.pop()` are O(1), and what to use instead when you need a queue.

---

Solutions in `correction_listes.md`.