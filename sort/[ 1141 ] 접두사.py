import sys

input = sys.stdin.readline
save = []

n = int(input())
words = [input().rstrip() for _ in range(n)]

words.sort(key = lambda x: len(x), reverse=True)
for word in words:
    for already_saved in save:
        if word == already_saved[:len(word)]:
            break
    else:
        save.append(word)

print(len(save))


