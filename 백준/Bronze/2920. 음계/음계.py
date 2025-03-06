li = list(map(int,input().split(' ')))
li_1 = sorted(li)
li_2 = sorted(li,reverse=True)

if li_1 == li:
    print('ascending')
elif li_2 == li:
    print('descending')
else:
    print('mixed')
