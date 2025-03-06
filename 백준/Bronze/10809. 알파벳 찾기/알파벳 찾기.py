alpha = 'abcdefghijklmnopqrstuvwxyz'
li = []
for i in range(len(alpha)):
    li.append(0)

n = input()


for i in range(len(alpha)):
    if alpha[i] in n:
        li[i] = n.index(alpha[i])
    else:
        li[i] = -1
    if i == (len(alpha)-1):
        print(li[i])
    else:
        print(li[i],end=' ')

