import sys
def input():
    return sys.stdin.readline()
M,N = map(int,input().split())

li = [i for i in range(2,M+1)]
p = min(li)
print(li,p)
for _ in range(len(li)):
    for i in range(len(li)):
        print('i =',i)
        print('li =',li)
        if li[i]%p == 0:
            li.remove(li[i])
            print(li[i])
            print(i,'전')
            i -= 1
            print(i,'후')