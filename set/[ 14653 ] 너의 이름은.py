import sys

input = lambda: sys.stdin.readline().rstrip()

N, K, Q = map(int, input().split())
people = set([chr(ch) for ch in range(ord('A'), ord('A')+N)])
people.remove('A')
messages = [[0, 0]] + [input().split() for _ in range(K)]

for i in range(Q, len(messages)):
    if messages[i][1] in people:
        people.remove(messages[i][1])

for i in range(Q-1, 0, -1):
    if messages[i][0] == messages[Q][0]:
        if messages[i][1] in people:
            people.remove(messages[i][1])
    else:
        break

people_list = sorted(list(people))
if messages[Q][0] == '0':
    print(-1)
else:
    print(*people_list)
