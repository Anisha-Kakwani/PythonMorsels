# It should work something like this:

# >>> matrix1 = [[1, -2], [-3, 4]]
# >>> matrix2 = [[2, -1], [0, -1]]
# >>> add(matrix1, matrix2)
# [[3, -3], [-3, 3]]
# >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
# >>> add(matrix1, matrix2)
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

def get_shape(listItem):
    return [len(matrix) for matrix in listItem]

def add(*lists):
    matrix_size = get_shape(lists[0])
    if any(get_shape(m) != matrix_size for m in lists):
        raise ValueError("Given matrices are not the same size.")
    combined=[]
    for items in zip(*lists):
        print(items)
        add=[]
        for numbers in zip(*items):
            addition=0
            for n in numbers:
                addition +=n
            add.append(addition)
        combined.append(add)
    return combined
add([[1, -2], [-3, 4]], [[2, -1], [0, -1]])