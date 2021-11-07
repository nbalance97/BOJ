import heapq
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T): 
    min_heap = []
    max_heap = []
    element_dict = defaultdict(lambda: 0)
    K = int(input())
    for __ in range(K):
        cmd, data = input().split()
        data = int(data)
        if cmd == 'I':
            heapq.heappush(min_heap, data)
            heapq.heappush(max_heap, -data)
            element_dict[data] += 1
        if cmd == 'D':
            if data == -1:
                while min_heap:
                    r = heapq.heappop(min_heap)
                    if element_dict[r] > 0:
                        element_dict[r] -= 1
                        break
            else:
                while max_heap:
                    r = heapq.heappop(max_heap)
                    r = -r
                    if element_dict[r] > 0:
                        element_dict[r] -= 1
                        break
    min_value = None
    max_value = None
    while min_heap:
        r = heapq.heappop(min_heap)
        if element_dict[r] > 0:
            min_value = r
            break
            
    while max_heap:
        r = heapq.heappop(max_heap)
        r = -r
        if element_dict[r] > 0:
            max_value = r
            break
    if min_value == None:
        print('EMPTY')
    else:
        print(max_value, min_value)
        
    
