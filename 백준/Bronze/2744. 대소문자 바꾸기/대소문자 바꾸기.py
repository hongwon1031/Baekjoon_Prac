a = input()
new_a=''
for char in a:
    if char.isupper():
        new_a += char.lower()
    elif char.islower():
        new_a += char.upper()
print(new_a)