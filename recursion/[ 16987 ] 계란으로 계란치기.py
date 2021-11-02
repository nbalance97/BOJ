import sys

input = lambda : sys.stdin.readline()

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

def solve(current):
    if current == len(eggs):
        count = 0
        for s, w in eggs:
            if s <= 0:
                count += 1
                
        return count
    # 현재 손에 든 계란 깨짐
    if eggs[current][0] <= 0:
        return solve(current+1)

    # 안깨진 계란이 남아있는지 체크하는 부분
    for i in range(len(eggs)):
        if i == current:
            continue
        if eggs[i][0] > 0:
            break
    else:
        return solve(current+1)
            
    # 시뮬레이션
    answer = 0
    for i in range(len(eggs)):
        if i == current:
            continue
        if eggs[i][0] <= 0:
            continue

        eggs[i][0] -= eggs[current][1]
        eggs[current][0] -= eggs[i][1]
        
        answer = max(answer, solve(current+1))

        # 다음 차례 가려면 기존에 빼주었던거 다시 더해주어야 함.
        eggs[i][0] += eggs[current][1]
        eggs[current][0] += eggs[i][1]
    
    return answer

print(solve(0))

    
