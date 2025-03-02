li = []
li_1 = []
for i in range(1, 29):
    li.append(int(input()))
for i in range(1, 31):
    if i in li:
        continue
    else:
        li_1.append(i)
print(min(li_1))
print(max(li_1))
