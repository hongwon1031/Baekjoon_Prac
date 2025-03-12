li = [list(map(str,input().split())) for _ in range(20)]
grade = {'A+':4.5,'A0':4.0,
        'B+':3.5,'B0':3.0,
        'C+':2.5,'C0':2.0,
        'D+':1.5,'D0':1.0,'F':0.0}

sum_1 = 0
sum_2 = 0
for i in range(len(li)):
    if li[i][2] == 'P':
        continue
    sum_1 += float(grade[li[i][2]])*float(li[i][1])
    sum_2 += float(li[i][1])


print(sum_1/sum_2)
