import sys

dictionary = {}

k = int(sys.stdin.readline().rstrip()) 
target = list(map(int, sys.stdin.readline().rstrip().split()))

real = list(sorted(set(target)))

for i,x in enumerate(real): # 좌표 작은 순으로 0,1,2, ... 대입하면 그게 압축
    dictionary[x] = i

for x in range(len(target)):
    target[x] = dictionary[target[x]]

print(*target)
