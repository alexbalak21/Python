# Sum of a list Write a function sum_list(lst) that returns the sum of all elements, without using sum().

def sum_list(lst):
    s = 0
    for n in lst:
        s+=n
    return s

print(sum_list([1,2,3,5]))