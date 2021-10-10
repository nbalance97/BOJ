import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        break
    word_dic = dict()
    for _ in range(n):
        word = input()
        word_dic[word.lower()] = word

    tot_item = list(word_dic.items())
    tot_item.sort(key=lambda x:x[0])
    print(tot_item[0][1])
