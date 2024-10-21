
def group_by_rhyme(a):

    c = []
    new_list = []

    i = 0
    while i < len(a):
        b = [a[i]]
        for j in range(i + 1, len(a)):
            if a[i][-1] == a[j][-1] and a[i][-2] == a[j][-2]:
                b.append(a[j])
            else:
                new_list.append(a[j])
        c.append(b)
        a = new_list[:]
        new_list = []


    return c

words = ['ana', 'banana', 'carte', 'arme', 'parte', 'katana']
print(group_by_rhyme(words))