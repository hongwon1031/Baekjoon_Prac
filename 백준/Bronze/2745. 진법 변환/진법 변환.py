import sys
def input():
    return sys.stdin.readline()
N,B = map(str,input().split())
B = int(B)
sum = 0
N = N[::-1]
for i in range(len(N)):
    if N[i].isalpha():
        n = ord(N[i]) - 55
    else:
        n = int(N[i])
    sum = sum + (B**i*n)
print(sum)


