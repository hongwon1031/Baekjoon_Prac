import sys
def input():
    return sys.stdin.readline()

def def_stack(stack):
    result = 1
    stack_count = 0
    for i in range(len(stack)):
        if stack[0] == ')':
            result = -1
            break
        
        if stack[i] == '(':
            stack_count += 1

        elif stack[i] == ')':
            if stack_count > 0:
                stack_count -= 1
            else:
                result = -1
        
    if stack_count != 0:
        result = -1

    return result

T = int(input())
for i in range(T):
    stack = input()
    
    if def_stack(stack) == 1:
        print('YES')
    elif def_stack(stack) == -1:
        print('NO')

