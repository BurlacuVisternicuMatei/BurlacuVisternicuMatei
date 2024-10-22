
def intersection(x, y):
    c = set()
    x1 = list(x)
    y1 = list(y)

    for i in range(0, len(x1)):
        for j in range(0, len(y1)):
            if x1[i] == y1[j]:
                c.add(x1[i])

    return c

def reunion(x, y):

    x1 = list(x)
    y1 = list(y)
    c = set(x1[:])

    for i in range(0, len(y1)):
        ok = 0
        for j in range(0, len(x1)):
            if y1[i] == x1[j]:
                ok = 1
        if ok == 0:
            c.add(y1[i])
    return c

def aminb(x, y):

    c = set()
    x1 = list(x)
    y1 = list(y)

    for i in range(0, len(x1)):
        ok = 0
        for j in range(0, len(y1)):
            if x1[i] == y1[j]:
                ok = 1
        if ok == 0:
            c.add(x1[i])

    return c


def bmina(x, y):

    c = set()
    x1 = list(x)
    y1 = list(y)

    for i in range(0, len(y1)):
        ok = 0
        for j in range(0, len(x1)):
            if y1[i] == x1[j]:
                ok = 1
        if ok == 0:
            c.add(y1[i])

    return c

def operations(*sets):

    a = {}
    for i in range(0, len(sets) - 1):
        for j in range(i + 1, len(sets)):
            print(sets[i])
            print(sets[j])
            str1 = repr(sets[i])
            str2 = repr(sets[j])

            str = str1
            str += "&"
            str += str2
            a.update({str : intersection(sets[i], sets[j])})

            str = str1
            str += "|"
            str += str2
            a.update({str: reunion(sets[i], sets[j])})

            str = str1
            str += "-"
            str += str2
            a.update({str: aminb(sets[i], sets[j])})

            str = str2
            str += "-"
            str += str1
            a.update({str: bmina(sets[i], sets[j])})

    return a


print(operations({1, 2}, {2, 3}))