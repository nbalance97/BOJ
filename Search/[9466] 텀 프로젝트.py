import sys
from collections import deque

input = sys.stdin.readline
case = int(input().rstrip())

def bfs(students, visited, num):
    # 팀에 속한 인원 수 리턴
    
    queue = deque()
    sequence = set()
    visited[num] = True
    if students[num] == num:
        return 1
    queue.append(students[num])
    sequence.add(num)
    
    while queue:
        current = queue.popleft()
        if visited[current]: # 이미 방문한 경우 뒤는 볼필요 없음
            break
        sequence.add(current)
        visited[current] = True
        
        if students[current] in sequence:
            start = students[current]
            idx = 0
            while True:
                idx += 1
                if students[start] == students[current]:
                    break
                else:
                    start = students[start]
                    
            # 그룹 인원 수 리턴
            return idx
        else:
            queue.append(students[current])

    return 0

for _ in range(case):
    N = int(input().rstrip())
    students = [0] + list(map(int, input().rstrip().split()))
    visited = [False] * len(students)
    count = 0
    
    for i in range(1, len(students)):
        if not visited[i]:
            count += bfs(students, visited, i)

    print(len(students)-1-count)
