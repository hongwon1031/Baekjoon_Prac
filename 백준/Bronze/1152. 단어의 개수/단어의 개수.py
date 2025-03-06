n = input()
if (n[0] == ' ') and (n[-1] == ' '):
    print(n.count(' ') -1)
elif (n[0] == ' ') or (n[-1] == ' '):
    print(n.count(' '))
else:
    print(n.count(' ') + 1)