# Find the maximum Write a function find_max(lst) that returns the largest number in a list, without using max().

def find_max(lst):
    return sorted(lst)[-1]


def find_max1(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max
