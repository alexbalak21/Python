# Matrix transpose Write a function transpose(matrix) that transposes a 2D list (list of lists), without using numpy.


def transpose(matrix):
    y_max = len(matrix)
    x_max = len(matrix[0])
    transposed = []
    for x in range(x_max):
        line = []
        for y in range(y_max):
            line.append(matrix[y][x])
        
        transposed.append(line)
    return transposed
        
# test case
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

#Expected result
expected = [
    [1, 4],
    [2, 5],
    [3, 6]
]


print(transpose(matrix))