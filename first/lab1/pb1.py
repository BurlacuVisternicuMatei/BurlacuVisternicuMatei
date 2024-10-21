input1 = input()
input1 = input1.split(" ")

def cmmdc(x, y):
    if x == 0:
        return y

    return cmmdc(y % x, x)

a=[]
for i in range (0, len(input1)):
    if input1[i].isdigit():
        a.append(int(input1[i]))

for i in range (1, len(a)):
    a[i] = cmmdc(a[i-1], a[i])

print(a[len(a) - 1])