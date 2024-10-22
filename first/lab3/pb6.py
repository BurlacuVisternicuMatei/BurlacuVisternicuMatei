
def counter(list):

    a = list
    b = set()#unic
    c = set()#duplicate
    for i in range(0, len(a)):
        if a[i] in b:
            b.remove(a[i])
            c.add(a[i])
        else:
            b.add(a[i])

    a = []
    a.append(len(b))
    a.append(len(c))
    a = tuple(a)
    return a


list1 = [1, 2, 3, 3, 5, 6, 1, 7, 4, 7, 9, 0]
print(counter(list1))
