'''a = input()
count = a.count(' ')
if (a[0] == ' ')or (a[-1] == ' '):
    count -= 1

print(count+1)

'''
a = input()
count = 0
for i in range(1,len(a)):
    if a[i] == ' ':
        count += 1
print(count)