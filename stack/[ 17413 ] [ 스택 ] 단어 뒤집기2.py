import sys

input = lambda : sys.stdin.readline().rstrip()

sentence = input()
stack = []
skip = False
answer = ''
for ch in sentence:
    if ch == '<':
        while stack:
            answer += stack.pop()
        skip = True
    elif ch == '>':
        answer += '>'
        skip = False
        continue

    if skip:
        answer += ch
    else:
        if ch == ' ':
            while stack:
                answer += stack.pop()
            answer += ch
        else:
            stack.append(ch)

while stack:
    answer += stack.pop()

print(answer)
