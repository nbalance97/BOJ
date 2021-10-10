import sys

input = lambda: sys.stdin.readline().rstrip()


N = int(input())

word_set = set()
for _ in range(N):
    word = input()
    check = False
    for i in range(len(word)):
        new_word = word[i:] + word[:i]
        if new_word in word_set:
            check = True
            break

    if not check:
        word_set.add(word)


print(len(word_set))
