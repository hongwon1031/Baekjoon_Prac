while True:
    li = list(map(int,input().split(' ')))
    if sum(li) == 0:
        break
    for i in range(len(li)):
        li[i] = li[i]**2
    li.sort()
    if li[0] + li[1] == li[2]:
        print("right")
    else:
        print('wrong')

