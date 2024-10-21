def palindrome(x):

    s1 = ''
    s = f"{x}"
    while x > 0:
        s1 += f"{int(x) % 10}"
        x = int(x/10)

    if s1 == s:
        return 1
    else :
        return 0


def tupleC(x):

    a = []
    maxim = 0

    for i in range(0, len(x)):
        if palindrome(x[i]) == 1:
            a.append(x[i])
            if x[i] > maxim:
                maxim = x[i]

    b = []
    b.append(a)
    b.append(maxim)
    tuple(b)
    return b

x = [1, 2, 3, 101, 423, 321, 12, 103, 9999]
print(tupleC(x))