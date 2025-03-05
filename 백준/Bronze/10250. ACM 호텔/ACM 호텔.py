n = int(input())
for k in range(n):
    H,W,N = map(int,input().split(' ')) # H = 6, W = 12
    for i in range(1,W+1):
        for j in range(1,H+1):
            N -= 1
            if N == 0:
                if  i < 10:
                    print(f'{j}0{i}')
                else:
                    print(f'{j}{i}')