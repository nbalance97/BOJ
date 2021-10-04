import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
hashtable = dict()

for _ in range(N):
    key, value = input().split()
    hashtable[key] = value

for _ in range(M):
    question = input()
    print(hashtable[question])
