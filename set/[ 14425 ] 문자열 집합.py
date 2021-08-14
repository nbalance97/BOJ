import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
string_set = set()

answer = 0

for i in range(N):
    string_set.add(sys.stdin.readline().rstrip('\n'))

for j in range(M):
    input_str = sys.stdin.readline().rstrip('\n')
    if input_str in string_set:
        answer += 1

print(answer)
