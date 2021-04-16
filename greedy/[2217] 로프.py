import sys

input = sys.stdin.readline

n = int(input().rstrip())

temp = []
for _ in range(n):
    temp.append(int(input().rstrip()))
answer = 0
temp.sort()
count = 0
# 정렬 후 오름차순으로 가장 큰 무게에서 내려가면서 비교 진행
for i in range(len(temp)-1, -1, -1):
    count += 1 
    # 병합하게 되면 모든 로프가 가장 낮은 로프의 무게만큼밖에 못쓰므로
    # 가장 낮은 로프의 무게 * 진행한 로프의 수로 최댓값 갱신
    answer = max(answer, temp[i] * count)
    
print(answer)
