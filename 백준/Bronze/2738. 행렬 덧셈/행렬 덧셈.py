N,M = map(int,input().split(' '))
size = N*M
li_1 = []
li_2 = []

for i in range(N):
    li_1.append(list(map(int,input().split(' '))))
for i in range(N):
    li_2.append(list(map(int,input().split(' '))))

li_3 = []

for i in range(N):
    for j in range(M):
        print(li_1[i][j]+li_2[i][j],end=' ')
    print('')
