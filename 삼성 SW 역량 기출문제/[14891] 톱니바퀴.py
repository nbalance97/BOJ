import sys

input = sys.stdin.readline

cogwheel = [[]]
# 12시 방향부터 시계방향 순서대로. 12, 1, 2, 3, ...
# 회전 시 6번과 2번(9시, 3시)
for _ in range(4):
    cogwheel.append(list(map(int, " ".join(input().rstrip()).split())))

def rotate(array):
    length = len(array)
    array = [array[-1]] + array[0:length-1]
    return array

def rotate_reverse(array):
    length = len(array)
    array = array[1:] + [array[0]]
    return array

def check_score(cogwheel):
    score = 0
    for t in range(1, len(cogwheel)):
        if cogwheel[t][0] == 1:
            score += (2 ** (t-1))
            
    return score
            
            

rotate_count = int(input().rstrip())
for i in range(rotate_count):
    rot_array = [0] * 5
    cogwheel_num, rot = map(int, input().rstrip().split())
    # 1인 경우 시계 방향, -1인 경우 반시계 방향

    rot_array[cogwheel_num] = rot # 자기 자신의 회전방향 저장
    
    temp = rot
    for j in range(cogwheel_num, 1, -1): # 왼쪽
        if cogwheel[j][6] != cogwheel[j-1][2]: # 맞물리는 쪽 다르다면
            # 맞물리는 쪽의 회전 방향 잡아줌
            temp = 1 if temp == -1 else -1
            rot_array[j-1] = temp
        else:
            # 맞물리는 쪽이 같으면 회전 안하므로 뒤에껏들도 안함
            break
        
    temp = rot
    for j in range(cogwheel_num, len(cogwheel)-1): # 오른쪽
        if cogwheel[j][2] != cogwheel[j+1][6]:
            temp = 1 if temp == -1 else -1
            rot_array[j+1] = temp
        else:
            # 맞물리는 쪽이 같으면 회전 안하므로 뒤에껏들도 안함
            break
    
    for j in range(1, len(rot_array)): # 회전 방향에 맞추어서 회전함
        if rot_array[j] == 0:
            continue
        if rot_array[j] == 1:
            cogwheel[j] = rotate(cogwheel[j])
        elif rot_array[j] == -1:
            cogwheel[j] = rotate_reverse(cogwheel[j])
            
print(check_score(cogwheel))
    
        
    
