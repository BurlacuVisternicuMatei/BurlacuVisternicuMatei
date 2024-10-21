from traceback import print_tb

input1 = input()
input1 = input1.upper()

maxim = 0
maxch = chr(0)
for i in range (0, 23):
    if input1.count(chr(48 + i)) > maxim:
        maxim = input1.count(chr(48 + i))
        maxch = chr(48 + i)

print(maxch)
print(maxim)