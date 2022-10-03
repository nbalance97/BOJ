import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input().strip())
persons = list(map(int, input().split()))
answer = 0

for permutation in permutations(persons):
    line = set()
    line.add(0)
    current = 0
    for person in permutation:
        current += person
        if current != 100:
            line.add(current)

    line_count = 0
    for i in range(0, 50):
        if i in line and (50 + i) in line:
            line_count += 1

    answer = max(answer, line_count)

print(answer)
