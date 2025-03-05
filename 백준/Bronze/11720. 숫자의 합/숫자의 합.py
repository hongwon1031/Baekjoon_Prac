n = int(input())
a = input()

result = sum(int(a[i]) for i in range(n))
print(result)