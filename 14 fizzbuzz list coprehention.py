# FizzBuzz using list comprehension Rewrite exercise 1 as a one-line list comprehension that returns a list of strings/numbers instead of printing.


print(["FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1, 101)])