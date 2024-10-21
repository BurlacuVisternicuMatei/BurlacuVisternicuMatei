input1 = int(input())
a = []
def fibonacci(x):
    a.append(0)
    a.append(1)
    a.append(1)
    for i in range (2, x - 1):
        a.append(a[i-1] + a[i])

    return a

print(fibonacci(input1))