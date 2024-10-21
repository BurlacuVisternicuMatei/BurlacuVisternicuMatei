
def ordering(*lists):

    a = []
    b = []
    c = []
    for i in lists:
        a.append(i)

    for i in range(0, len(a[0])):
        for j in range(0, len(a)):
            b.append(a[j][i])
        c.append(tuple(b))
        b = []

    return c

list1 = [1,2,3]
list2 = [5,6,7]
list3 = ["a", "b", "c"]
print(ordering(list1, list2, list3))