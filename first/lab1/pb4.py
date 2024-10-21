input1 = input()

for i in range(1, len(input1)):
    if input1[i - 1] == '_':
        continue
    if input1[i].isupper():
        input1 = input1[0:i] + '_' + input1[i:]

input1 = input1.lower()
print(input1)