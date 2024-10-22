
def cmp_dict(dict1, dict2):

    ok = 1
    for i in dict1:
        if i in dict2 == False:
            ok = 0
            break
        elif dict1.get(i) != dict2.get(i):
        #elif cmp_dict(dict1.get(i), dict2.get(i)) == 0 :
            ok = 0
            break


    return ok

dict1 = {'a': 2, 'c': 1, 'd': 1, 'f': 1, 'l': 1, 'm': 1, 't': 2, 'u': 3}
dict2 = {'a': 2, 'c': 1, 'd': 2, 'f': 1, 'l': 1, 'm': 1, 't': 2, 'u': 3}
print(cmp_dict(dict1, dict2))
print(dict1 == dict2)