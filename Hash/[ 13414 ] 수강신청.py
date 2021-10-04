import sys

input = lambda : sys.stdin.readline().rstrip()

K, L = map(int, input().split())

hashtable = dict()
idx = 0
for _ in range(L):
    idx += 1
    sid = input()
    hashtable[sid] = idx

sugang_data = sorted(hashtable.items(), key=lambda x:x[1])
sugang_data = sugang_data[:K]

for student, _ in sugang_data:
    print(student)
