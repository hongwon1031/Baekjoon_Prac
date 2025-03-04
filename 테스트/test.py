import sys
n = sys.stdin.readline()


for i in range(int(n)):
    a = sys.stdin.readline().rstrip()
    a,b = a.split(' ')
    print(int(a)+int(b))





'''1 1
12 34
5 500
40 60
1000 1000'''