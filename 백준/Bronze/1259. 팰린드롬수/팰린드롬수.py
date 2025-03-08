k = 0
while True:
    k += 1
    a = input()
    if a == '0':
        break
    result = True
    for i in range(len(a)//2):
        if a[i] == a[-i -1]:
            result = True
            continue
        else:
            result = False
            break

    if result:

        print('yes')
    else:

        print('no')