import sys

input = sys.stdin.readline
N = int(input())

sequences = list(map(int, input().split()))
S = int(input())

for i in range(len(sequences)):
    max_number = max(sequences[i:min(len(sequences), i + S + 1)])
    max_number_index = sequences.index(max_number)

    while max_number_index > i:
        sequences[max_number_index-1], sequences[max_number_index] = sequences[max_number_index], sequences[max_number_index-1]
        S = S - 1
        max_number_index = max_number_index - 1

print(" ".join(map(str, sequences)))
