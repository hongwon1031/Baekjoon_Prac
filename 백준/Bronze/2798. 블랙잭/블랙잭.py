N,M = map(int,input().split(' '))
li = list(map(int,input().split(' ')))
li_1 = li[:N]
li_2 = []
#N = 7
for i in range(N-2):  #0~4
    for j in range(i+1,N-1): #i+1 ~ 5
        for k in range(j+1,N): # j+1 ~ 6
            if li_1[i]+li_1[j]+li_1[k] <= M:
                li_2.append(li_1[i]+li_1[j]+li_1[k])
print(max(li_2))