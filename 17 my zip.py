# Custom zip Implement your own version of zip() called my_zip(*iterables) using a generator.



def my_zip(*iterables):
    # Get the minimum length of the input iterables
    min_length = min(len(iterable) for iterable in iterables)
    
    # Use a generator to yield tuples of elements from each iterable
    for i in range(min_length):
        yield tuple(iterable[i] for iterable in iterables)
       

            
       
   
            
    


print(list(my_zip(
    [1, 2, 3],
    ["a", "b", "c"],
    [True, False, True],
    ["x", "y"]
)))    