import sys

input = sys.stdin.readline

sequence = list(map(int, input().rstrip().split()))

ascending = False
descending = False

for i in range(1, len(sequence)):
    if sequence[i] > sequence[i-1]:
        ascending = True
    else:
        descending = True

if ascending and not descending:
    print("ascending")
elif descending and not ascending:
    print("descending")
else:
    print("mixed")
