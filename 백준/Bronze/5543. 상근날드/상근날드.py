import sys
def input():
    return sys.stdin.readline()
burger = [int(input()) for _ in range(3)]
juice = [int(input()) for _ in range(2)]
min = 4000
for i in range(len(burger)):
    for j in range(len(juice)):
        price = burger[i]+juice[j] - 50
        if price < min:
            min = price
print(min)