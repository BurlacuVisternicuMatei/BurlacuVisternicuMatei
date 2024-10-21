matrix = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [9, 10, 11, 12]]

def put0(x):
    for i in range(0, len(x[0])):
        for j in range(0, len(x[0])):
            if j < i:
                x[i][j] = 0

    return x

put0(matrix)
print(matrix)