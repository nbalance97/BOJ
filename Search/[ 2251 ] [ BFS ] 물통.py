import sys
from collections import deque

def bfs(max_a, max_b, max_c):
    answer = set()
    queue = deque()
    visited = set()
    queue.append([0, 0, max_c])
    visited.add(tuple([0, 0, max_c]))

    while queue:
        aL, bL, cL = queue.popleft()
        if aL == 0:
            answer.add(cL)

        # a -> b, c
        if aL > 0:
            if bL + aL <= max_b and (0, bL+aL, cL) not in visited:
                visited.add((0, bL+aL, cL))
                queue.append([0, bL+aL, cL])
            elif bL + aL > max_b and ((bL+aL)-max_b, max_b, cL) not in visited:
                visited.add(((bL+aL)-max_b, max_b, cL))
                queue.append([(bL+aL)-max_b, max_b, cL])

            if cL + aL <= max_c and (0, bL, cL+aL) not in visited:
                visited.add((0, bL, cL+aL))
                queue.append([0, bL, cL+aL])
            elif cL + aL > max_c and ((cL+aL)-max_c, bL, max_c) not in visited:
                visited.add(((cL+aL)-max_c, bL, max_c))
                queue.append([(cL+aL)-max_c, bL, max_c])

        # b -> a, c
        if bL > 0:
            if bL + aL <= max_a and (bL+aL, 0, cL) not in visited:
                visited.add((bL+aL, 0, cL))
                queue.append([bL+aL, 0, cL])
            elif bL + aL > max_a and (max_a, (bL+aL)-max_a, cL) not in visited:
                visited.add((max_a, (bL+aL)-max_a, cL))
                queue.append([max_a, (bL+aL)-max_a, cL])

            if cL + bL <= max_c and (aL, 0, cL+bL) not in visited:
                visited.add((aL, 0, cL+bL))
                queue.append([aL, 0, cL+bL])
            elif cL + bL > max_c and (aL, (cL+bL)-max_c, max_c) not in visited:
                visited.add((aL, (cL+bL)-max_c, max_c))
                queue.append([aL, (cL+bL)-max_c, max_c])

        # c -> a, b
        if cL > 0:
            if cL + aL <= max_a and (cL+aL, bL, 0) not in visited:
                visited.add((cL+aL, bL, 0))
                queue.append([cL+aL, bL, 0])
            elif cL + aL > max_a and (max_a, bL, (cL+aL)-max_a) not in visited:
                visited.add((max_a, bL, (cL+aL)-max_a))
                queue.append([max_a, bL, (cL+aL)-max_a])

            if cL + bL <= max_b and (aL, bL+cL, 0) not in visited:
                visited.add((aL, bL+cL, 0))
                queue.append([aL, bL+cL, 0])
            elif cL + bL > max_b and (aL, max_b, (bL+cL)-max_b) not in visited:
                visited.add((aL, max_b, (bL+cL)-max_b))
                queue.append([aL, max_b, (bL+cL)-max_b])
                
    return answer
            
        
    

a, b, c = map(int, sys.stdin.readline().rstrip().split())
temp = sorted(list(bfs(a, b, c)))
print(*temp)
