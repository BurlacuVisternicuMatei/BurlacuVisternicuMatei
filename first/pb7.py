input1 = input()

ok = 0
i = 0

while ok == 0 :
    if ord(input1[i]) >= 48 and ord(input1[i]) <= 57:
        ok = 1
        s = input1[i:]
    i += 1

ok = 0
i = 0

while ok == 0 :
    if ord(s[i]) < 48 or ord(s[i]) > 57:
        ok = 1
        s = s[:i]
    i += 1

print(s)