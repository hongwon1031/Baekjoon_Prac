import sys
def input():
    return sys.stdin.readline()
li = []

max = 0
for _ in range(5):
    a = input().strip()
    li.append(a)
    if len(a) >= max:
        max = len(a)
for k in range(5):
    if len(li[k]) >= max:
        continue
    else:

        for _ in range(max - len(li[k])):
            li[k] = li[k]+' '


li_1 = []

for i in range(max):
    for n in range(5):
        if li[n][i] ==' ':
            continue
        else:
            li_1.append(li[n][i])
for j in range(len(li_1)):
    print(li_1[j],end='')


