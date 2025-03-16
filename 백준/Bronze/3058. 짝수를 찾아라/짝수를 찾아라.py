import sys
def input():
    return sys.stdin.readline()
T = int(input())

for _ in range(T):
    li_1 = []
    li = list(map(int,input().split()))
    for i in range(len(li)):
        if li[i]%2 == 0:
            li_1.append(li[i])
    print(sum(li_1), min(li_1))

    