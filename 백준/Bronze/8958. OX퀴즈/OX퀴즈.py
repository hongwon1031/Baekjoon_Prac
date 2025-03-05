n = int(input())
for k in range(n):
    a = input()
    li = list(a)
    sum = 0
    for i in range(len(li)):
        if li[i] == 'O':
            score = 0
            for j in range(i,-1,-1):
                if li[j] == 'O':
                    score += 1
                elif li[j] == 'X':
                    break     
        elif li[i] == 'X':
            score = 0
        sum += score
    print(sum)