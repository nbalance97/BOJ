import sys

input = lambda: sys.stdin.readline().rstrip()

N, Hatk = map(int, input().split())

dungeons = [list(map(int, input().split())) for _ in range(N)]

left = 1
right = int(10e16)
answer = 0
while left <= right:
    mid = (left + right) // 2
    current_HP = mid
    current_ATK = Hatk
    status = True
    for dungeon in dungeons:
        t, a, h = dungeon
        if t == 1:
            step = h // current_ATK
            if h % current_ATK == 0:
                step -= 1
            current_HP -= a * step
            if current_HP <= 0:
                status = False
                break
        elif t == 2:
            current_HP = min(current_HP+h, mid)
            current_ATK = current_ATK + a
        
    if status:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
    
