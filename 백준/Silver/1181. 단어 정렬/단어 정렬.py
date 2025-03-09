import sys

N = int(sys.stdin.readline())
li = [input().strip() for _ in range(N)]
li = list(set(li))  


sorted_li = sorted(li, key=lambda x: (len(x), x))

for s in sorted_li:
    print(s)
