#  Remove duplicates Write a function remove_duplicates(lst) that returns a list with duplicates removed, preserving order.

def remove_duplicates(lst :list[int|float]):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
        seen.add(x)
    return result
        
        
print(remove_duplicates([1,2,3,5,1,2,3,5,1,2,3,5,1,2,3,5,1,2,3,5]))