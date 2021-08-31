import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = [int(input().rstrip()) for _ in range(N)]

array.sort()
a, b = 0, 0
answer = int(10e9)
while b < len(array):
    subtraction = array[b] - array[a]
    
    if subtraction >= M:
        answer = min(answer, subtraction)

    if subtraction <= M:
        b = b + 1
    else:
        a = a + 1
    
    if a > b:
        b = b + 1

print(answer)
