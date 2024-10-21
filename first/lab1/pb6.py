input1 = input()

def palindrome(x):

    s1 = ''
    s = f"{x}"
    while x > 0:
        s1 += f"{int(x) % 10}"
        x = int(x/10)

    if s1 == s:
        return 1
    else :
        return 0


print(palindrome(int(input1)))