import sys

input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    org_a, org_b = input().rstrip().split()
    # 두개의 문자열 오름차순 정렬
    a = list(org_a)
    b = list(org_b)
    a.sort()
    b.sort()
    
    # 길이 다르면 애너그램 아님
    if len(a) != len(b):
        print("%s & %s are NOT anagrams."%(org_a, org_b))
    else:
        for i in range(len(a)):
            # 문자중 다른게 있으면 애너그램 아님
            if a[i] != b[i]:
                print("%s & %s are NOT anagrams."%(org_a, org_b))
                break
        else:
            # 모두 통과한 경우 애너그램
            print("%s & %s are anagrams."%(org_a, org_b))
