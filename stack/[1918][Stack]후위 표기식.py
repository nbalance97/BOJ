import sys
 
t = sys.stdin.readline().rstrip()
 
op_stack = []
answer = ''
p = ['+', '-', '*', '/', '(', ')']
for s in t:
    if s not in p:
        answer += s
    elif s == '+' or s == '-':
        while op_stack:
            if op_stack[-1] != '(':
                answer += op_stack.pop()
            else:
                break
        op_stack.append(s)
    elif s == '*' or s == '/':
        while op_stack:
            if op_stack[-1] == '*' or op_stack[-1] == '/':
                answer += op_stack.pop()
            else:
                break
        op_stack.append(s)
    elif s == ')':
        while op_stack:
            if op_stack[-1] != '(':
                answer += op_stack.pop()
            else:
                op_stack.pop()
                break
    else:
        op_stack.append(s)
 
while op_stack:
    answer += op_stack.pop()
 
print(answer)
