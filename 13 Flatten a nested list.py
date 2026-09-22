# Flatten a nested list Write a function flatten(lst) that flattens an arbitrarily nested list, e.g. [1, [2, [3, 4], 5]] -> [1, 2, 3, 4, 5].

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result





print(flatten([1, [2, [3, 4], 5]]))





