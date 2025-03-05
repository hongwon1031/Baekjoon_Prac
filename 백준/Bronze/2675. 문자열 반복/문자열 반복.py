a = int(input())
for j in range(a):
    b1,b2 = map(str,input().split(' '))
    li = [b2[x]*int(b1) for x in range(len(b2))]
    for i in range(len(li)):
        if i == len(li)-1:
            print(li[i])
        else:
            print(li[i],end='')
        
