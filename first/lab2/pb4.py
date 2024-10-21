input1 = input() #note
input2 = input() #ordine
input3 = int(input()) #start

order = []
def toInt(x):
    if x != '':
        order.append(int(x))

def music(notes, order, start):

    a = []
    a.append(notes[start])
    old = start

    for i in range(0 , len(order)):
        a.append(notes[0 + (old + order[i]) % len(notes)]) ####?????
        old = 0 + (old + order[i]) % len(notes)

    return a

input2 = input2.split(" ")
input1 = input1.split(" ")
for i in range(0, len(input2)): #scoatem spatiile inutile si transformam in lista de int
    toInt(input2[i])

print(music(input1, order, input3))