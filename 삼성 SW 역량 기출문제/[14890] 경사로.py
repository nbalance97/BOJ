import sys

input = sys.stdin.readline
N, L = map(int, input().rstrip().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

answer = 0

# 행 기준으로
for row in range(N):
    succeed = True
    
    temp = [False] * N
    for i in range(1, N):
        last = i - 1 # 루프 기준점 이전
        
        if matrix[row][last] != matrix[row][i]:
            # 높이 차이가 1이상이면 실패
            if abs(matrix[row][last] - matrix[row][i]) >= 2:
                succeed = False
                break

            if matrix[row][last] < matrix[row][i]: # 오른쪽이 더 크면 왼쪽 L칸 검사해야
                for j in range(1, L+1):
                    if i - j < 0 or temp[i-j] == True: # 칸 벗어나거나 이미 그어진 경사로라면 실패
                        succeed = False
                        break
                    
                    if matrix[row][i-j] == matrix[row][last]: 
                        temp[i-j] = True
                    else:
                        succeed = False
                        break
                
            else:
                for j in range(1, L+1): # 왼쪽이 더 크면 오른쪽 L칸 검사해야 함.
                    if last + j >= N or temp[last + j] == True:
                        succeed = False
                        break

                    if matrix[row][last + j] == matrix[row][i]:
                        temp[last + j] = True
                    else:
                        succeed = False
                        break
                    
            if not succeed:
                break

    if succeed:
        answer += 1

# 열 기준으로
for col in range(N):
    succeed = True
    
    temp = [False] * N
    for i in range(1, N):
        last = i - 1 # 루프 기준점 이전
        
        if matrix[last][col] != matrix[i][col]:
            # 높이 차이가 1이상이면 실패
            if abs(matrix[last][col] - matrix[i][col]) >= 2:
                succeed = False
                break

            if matrix[last][col] < matrix[i][col]: # 아래쪽이 더 크면 위쪽 L칸 검사해야
                for j in range(1, L+1):
                    if i - j < 0 or temp[i-j] == True: # 칸 벗어나거나 이미 그어진 경사로라면 실패
                        succeed = False
                        break
                    
                    if matrix[i-j][col] == matrix[last][col]: 
                        temp[i-j] = True
                    else:
                        succeed = False
                        break
                
            else:
                for j in range(1, L+1): # 위쪽이 더 크면 아래쪽 L칸 검사해야 함.
                    if last + j >= N or temp[last + j] == True:
                        succeed = False
                        break

                    if matrix[last + j][col] == matrix[i][col]:
                        temp[last + j] = True
                    else:
                        succeed = False
                        break
                    
            if not succeed:
                break

    if succeed:
        answer += 1
                
print(answer)


        

    
