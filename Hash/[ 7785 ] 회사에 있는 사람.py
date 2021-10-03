import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

dictionary = {}
for _ in range(n):
    person, method = input().split()
    if method == 'enter':
        dictionary[person] = 1
    elif method == 'leave':
        dictionary[person] = 0

people = []
for key, value in dictionary.items():
    if value == 1:
        people.append(key)

people.sort(reverse=True)
for p in people:
    print(p)
