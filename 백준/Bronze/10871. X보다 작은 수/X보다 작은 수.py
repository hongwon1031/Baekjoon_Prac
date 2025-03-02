# 1 10 4 9 2 3 8 5 7 6
N,X = map(int,input().split(' ')) # 10 5
B = list(map(int,input().split(' '))) # 1 10 4 9 2 3 8 5 7 6
B_new = []
for i in range(0,N):
    if B[i] < X:
        print(B[i],end=' ')



