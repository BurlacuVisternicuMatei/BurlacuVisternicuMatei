
def counter(*lists):
    a = []
    b = []

    for number in lists:
        a.append(number)

    x = a[len(a) - 1] #the number to count by

    for i in range(0, len(a) - 1): #parcurgem fiecare lista in parte - excludem x
        for j in range(0, len(a[i])):
            b.append(a[i][j])

    a = []
    for i in range(0, len(b)):
        if b.count(b[i]) == x:
            if a.count(b[i]) == 0:
                a.append(b[i])

    return a

list1 = [1,2,3]
list2 = [2,3,4]
list3 = [4,5,6]
list4 = [4,1, "test"]
x = 2

print(counter(list1, list2, list3, list4, x))