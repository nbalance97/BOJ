import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    sequence = []
    loopcount = n // 10 + 1
    if n % 10 == 0:
        loopcount -= 1
        
    for __ in range(loopcount):
        sequence += list(map(int, input().split()))
    left = []
    right = []
    answer = []
    for i, s in enumerate(sequence):
        heapq.heappush(left, -s)
        while len(left) > len(right):
            heapq.heappush(right, -heapq.heappop(left))
        while left and right and -left[0] >= right[0]:
            heapq.heappush(right, -heapq.heappop(left))

        while len(right) > len(left)+1:
            heapq.heappush(left, -heapq.heappop(right))
        
        if (i+1) % 2 == 1:
            answer.append(right[0])

    print(len(answer))
    printloop = len(answer) // 10 + 1
    if len(answer) % 10 == 0:
        printloop -= 1
    for i in range(printloop):
        print(*answer[i*10:(i+1)*10])
            
