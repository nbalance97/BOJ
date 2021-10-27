import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
words = [input() for _ in range(N)]

def get_value(word):
    value = 0
    for w in word:
        if w.isdigit():
            value += int(w)

    return value

words.sort(key=lambda x:(len(x), get_value(x), x))
for word in words:
    print(word)
