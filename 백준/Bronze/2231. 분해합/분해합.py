n = int(input())
li = []
n_str = str(n)  
n_len = len(n_str)  

for i in range(9*n_len+1):    
    a = n - i
    if a < 0:
        break
    a = str(a)
    sum_a = 0
    for j in range(len(a)):          
        sum_a = sum_a + int(a[j])
    sum_a = sum_a + int(a)
    if sum_a == n:
        li.append(a)    

if len(li) == 0:
    print(0)
else:

    print(min(li))
