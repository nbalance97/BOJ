import sys

save = [False] * 100001

p = int(sys.stdin.readline().rstrip())
temp = list(map(int, sys.stdin.readline().rstrip().split()))

for i in temp:
    save[i + 1000] = True # 범위가 -1000~1000이므로 음수 처리 

for i in range(len(save)):
    if save[i]:
        print(i-1000, end=" ")
        
