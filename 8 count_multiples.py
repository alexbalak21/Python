# 8. FizzBuzz with a twist — counting Write a function count_multiples(lst, n) that returns how many numbers in lst are divisible by n.

def count_multiples(lst, n):
    c = 0
    for x in lst:
        if x % n == 0:
            c+=1
    return c


def count_multiples1(lst, n):
    return sum(1 for x in lst if x % n == 0)



print(count_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)) # Output: 5