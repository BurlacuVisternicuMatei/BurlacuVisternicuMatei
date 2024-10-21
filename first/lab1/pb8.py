input1 = input()
x = int(input1)

def bits(x):
    c = 0
    y = int(x)
    while y > 0:
        if int(y) % 2 == 1:
            c += 1
        y /= 2
    return c

print(bits(x))