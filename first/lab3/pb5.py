
def verify(ss, dd):

    occ = 0

    for i in dd:
        for j in ss:
            if i in j:
                occ = 1
                if dd.get(i).startswith(j[1]) == 0:
                    return False
                elif dd.get(i).endswith(j[3]) == 0:
                    return False
                elif j[2] not in dd.get(i) :
                    return False
        if occ == 0:
            return False #am parcurs setul de reguli o data pentru o cheie si nu am gasit o
        occ = 0

    return True




s = set()
s.add(("key1", "", "inside", ""))
s.add(("key2", "start", "middle", "winter"))
#d= {"key1": "come inside, it's too cold out", "key3": "this is not valid", "key2": "startmiddlewinter"}
d= {"key1": "come inside, it's too cold out", "key2": "start middle winter"}

print(verify(s, d))
