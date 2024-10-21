input1 = input()

a = input1.split(" ")

def isprime(x):

    y = int(x)

    if y == 1:
        return 0
    if y == 2:
        return 1
    if y % 2 == 0:
        return 0

    i = 3
    while i * i <= y:
        if y % i == 0:
            return 0
        i += 2

    return 1

def primeList(a):

    b = []
    for i in range(0, len(a)):
        if isprime(a[i]) == 1:
            b.append(a[i])

    return b

print(primeList(a))
