import sys

input = lambda: sys.stdin.readline().rstrip()
sequence = list(map(int, list(input())))

answer = 0
for length in range(2, len(sequence)+1, 2):
    for i in range(len(sequence) - length + 1):
        left = sequence[i:i+length//2]
        right = sequence[i+length//2:i+length]
        if sum(left) == sum(right):
            answer = max(answer, length)

print(answer)
