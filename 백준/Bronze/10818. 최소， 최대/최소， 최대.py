N = int(input())
number = list(map(int,input().split(' ')))

print(min(number[:N]),max(number[:N]))
