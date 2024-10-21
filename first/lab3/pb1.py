#la fel ca lab2_pb3??
input1 = input()
input2 = input()

a = input1.split(" ")
b = input2.split(" ")

def intersection(x, y):
    c = []

    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i] == y[j]:
                c.append(x[i])

    return c

def reunion(x, y):
    c = x[:]

    for i in range(0, len(y)):
        ok = 0
        for j in range(0, len(x)):
            if y[i] == x[j]:
                ok = 1
        if ok == 0:
            c.append(y[i])
    return c

def aminb(x, y):

    c = []

    for i in range(0, len(x)):
        ok = 0
        for j in range(0, len(y)):
            if x[i] == y[j]:
                ok = 1
        if ok == 0:
            c.append(x[i])

    return c


def bmina(x, y):

    c = []

    for i in range(0, len(y)):
        ok = 0
        for j in range(0, len(x)):
            if y[i] == x[j]:
                ok = 1
        if ok == 0:
            c.append(y[i])

    return c

def res(x, y):
    c = []

    c.append(intersection(x, y))
    c.append(reunion(x, y))
    c.append(aminb(x, y))
    c.append(bmina(x, y))

    return c

print(res(a, b))