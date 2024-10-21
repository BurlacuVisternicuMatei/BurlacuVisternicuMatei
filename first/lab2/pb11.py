
def cmp(a, b):
    if a[1][2] > b[1][2]:
        return 1
    elif a[1][2] == b[1][2]:
        return 0
    else:
        return -1

a = [('abc', 'bcd'), ('abc', 'zza')]

a.sort(key=lambda x: x[1][2])
print(a)