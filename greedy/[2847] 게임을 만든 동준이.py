import sys

input = sys.stdin.readline

n = int(input().rstrip())

temp = []
for _ in range(n):
    temp.append(int(input().rstrip()))

ans = 0
# 마지막 단계에서부터 해야 함.. 앞에서부터 하면
# 꼬이게 될 가능성 농후

if len(temp) == 1:
    print(0)
    sys.exit(0)

for i in range(n-1, 0, -1):
    if temp[i] <= temp[i-1]:
        ans += (temp[i-1]-temp[i]+1)
        temp[i-1] = temp[i]-1
print(ans)
