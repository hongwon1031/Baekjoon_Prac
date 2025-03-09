def sosu(x):
    count = 0
    for i in range(1,x+1):
        if x%i == 0:
            count += 1
        
    if count == 2:
        return 1
    else:
        return  0


n = int(input())
li = list(map(int,input().split(' ')))

result = 0
for i in range(n):
    result = result + sosu(li[i])

print(result)