input1 = input()

def dictionary(x):

    x = x.lower()
    a = {}
    for i in range(0, 26):
        if x.count(chr(ord('a') + i)):
            a.update({chr(ord('a') + i) : x.count(chr(ord('a') + i))})

    return a

print(dictionary(input1))


