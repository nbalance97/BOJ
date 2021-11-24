import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

wton = {'ZERO': 0, 'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4,
        'FIVE': 5, 'SIX':6, 'SEVEN': 7, "EIGHT": 8, "NINE": 9}
ntow = {str(k):v for v, k in wton.items()}

s = input()
for k, v in wton.items():
    s = s.replace(k, str(v))

sp = deque()
op = []
ch = ''
end = False
for c in s:
    if c in ['+', '-', 'x', '/', '=']:
        if ch == '':
            end = True
            break
        if c != '=':
            op.append(c)
        sp.append(int(ch))
        ch = ''
    elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        ch += c
    else:
        end = True
        break
if end:
    print('Madness!')
else:
    for o in op:
        a = sp.popleft()
        b = sp.popleft()
        if o == 'x':
            sp.appendleft(a * b)
        elif o == '-':
            sp.appendleft(a - b)
        elif o == '/':
            if a < 0:
                a = -a
                sp.appendleft(-(a // b))
            else:
                sp.appendleft(a // b)
        elif o == '+':
            sp.appendleft(a + b)
    calc = str(sp[0])
    minus = False
    if calc[0] == '-':
        minus = True
        calc = calc[1:]
    answer = ''
    for c in calc:
        answer += ntow[c]
    answer = '-'+answer if minus else answer
    print(s)
    print(answer)
