
def taller(x):

    small = []
    for i in range(0, len(x[0])): #merge pe prima linie stanga dreapta
        j = 1
        height = x[0][i]

        while j < len(x):
            if x[j][i] <= height:
                small.append(tuple([j, i]))
            else:
                height = x[j][i]
            j += 1

    return small


matrix = [[1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]]

print(taller(matrix))
