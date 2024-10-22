
def loop(mapping):

    a = list()
    ok = 1
    currentKey = 'start'

    while ok:
        if currentKey in mapping:
            if mapping.get(currentKey) in a:
                ok = 0
            else:
                currentKey = mapping.get(currentKey)
                a.append(currentKey)
        else:
            ok = 0

    return a


mapp = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(mapp))