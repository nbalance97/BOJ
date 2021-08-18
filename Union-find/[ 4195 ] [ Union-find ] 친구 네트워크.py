import sys
input = sys.stdin.readline

total_case = int(input().rstrip())

def find(parent, group, a):
    if parent[a] != a:
        parent[a] = find(parent, group, parent[a])
        group[a] = group[parent[a]]
    return parent[a]

def union(parent, group, a, b):
    p1 = find(parent, group, a)
    p2 = find(parent, group, b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

for i in range(total_case):
    F = int(input().rstrip())
    member = dict()
    count = 0
    parent = [-1] * 200001
    group = [0] * 200001
    for _ in range(F):
        person1, person2 = input().rstrip().split()

        # 새로운 멤버 추가
        if member.get(person1) == None:
            parent[count] = count
            member[person1] = count
            group[count] = 1
            count += 1
        if member.get(person2) == None:
            parent[count] = count
            member[person2] = count
            group[count] = 1
            count += 1

        # 두 그룹 합침
        par1 = find(parent, group, member[person1])
        par2 = find(parent, group, member[person2])
        if par1 != par2:
            union(parent, group, par1, par2)
            # 그룹 인원수 합침
            temp = group[par1] + group[par2]
            group[par1] = temp
            group[par2] = temp
    
        # 위 과정에서는 부모의 인원수만 바뀌므로   
        # find 한번 더 호출해서 그룹 멤버 수 조정
        find(parent, group, member[person1])
        find(parent, group, member[person2])

        group_count = group[member[person1]]
        print(group_count)
        
        
