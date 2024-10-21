input1 = input()

a = []
i = 1
a.append(list(input1))
while i < len(input1):
    a.append(list(input()))
    i += 1

s = ''

j = 0
while j <= len(input1) - 2:

    i = j
    while i < len(input1) - j:
        s += a[j][i]
        i += 1

    i = j + 1
    while i < len(input1) - j:
        s += a[i][len(input1) - 1 - j]
        i += 1

    i = len(input1) - 2 - j
    while i >= 0 + j:
        s += a[len(input1) - 1 - j][i]
        i -= 1

    i = len(input1) - 2 - j
    while i >= 1 + j:
        s += a[i][0 + j]
        i -= 1

    j += 1


print(s)
