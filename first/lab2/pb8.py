
def asciiDiv(y, flag, x = 1):

    a = []

    if flag:
        z = 0
    else:
        z = 1

    b = []
    for i in range(0, len(y)):
        for j in range(0, len(y[i])):
            print(ord(y[i][j]))
            if int(ord(y[i][j])) % x == z:
                b.append(y[i][j])
        a.append(b)
        b = []

    return a

strings = ["test", "hello", "lab002"]
print(asciiDiv(strings, False, 2))
