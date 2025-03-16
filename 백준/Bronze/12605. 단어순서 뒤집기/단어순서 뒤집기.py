import sys
def input():
    return sys.stdin.readline()
N = int(input())
for j in range(N):
    a = str(input()).strip()
    li = (a.split(' '))
    
    print(f'Case #{j+1}: ',end='')
    for i in range(len(li)-1,-1,-1):
        if i == 0:
            print(li[i])    
        else:
            print(li[i],end=' ')

    