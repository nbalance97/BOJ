import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

match = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5,
         6: 6, 7: 3, 8: 7, 9: 6}

def calculate_match(i, j):
    temp = i + j
    target = [[i%10, i//10], [j%10, j//10], [temp%10, temp//10]]
    matches = 0
    for p, q in target:
        matches += match[p] + match[q]

    return matches
    

N = N - 4
end = False
for i in range(100):
    for j in range(100):
        if i + j >= 100:
            continue
        if calculate_match(i, j) == N:
            end = True
            print("%s+%s=%s"%(str(i).zfill(2),
                              str(j).zfill(2),
                              str(i+j).zfill(2)))
        if end:
            break
    if end:
        break

if not end:
    print('impossible')
                  
