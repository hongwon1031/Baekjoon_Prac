H,M = map(int,input().split(' '))
new_M = M - 45
if new_M < 0:
    new_M = (60 + M) - 45
    H = H - 1
if H < 0:
    H = 23
print(H,new_M)