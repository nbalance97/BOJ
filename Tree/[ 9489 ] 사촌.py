import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

while True:
    n, k = map(int, input().split())

    if n == 0 and k == 0:
        break
    
    parent = [0] * 1000001
    heap = []
    numbers = list(map(int, input().split()))

    pre = -1
    par = 0
    for number in numbers:
        if pre == -1:
            heapq.heappush(heap, number)
            pre = number
            continue

        if number != pre + 1:
            par = heapq.heappop(heap)
            
        heapq.heappush(heap, number)
        parent[number] = par
        pre = number

    pparent_num = parent[parent[k]]

    if pparent_num == 0:
        print(0)
        continue
    
    count = 0
    for i in numbers:
        if parent[i] != parent[k] and parent[parent[i]] == pparent_num:
            count += 1
        
    print(count)
