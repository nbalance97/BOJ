import sys
from collections import Counter

input = sys.stdin.readline

words = []
while (data := input().rstrip()) != "-":
    words.append(Counter(data))

while (table := input().rstrip()) != "#":
    answer_count = []
    visited = set()
    counter = Counter(table)
    for ch in set(table):
        needed = ch
        count = 0
        for word in words:
            if word.get(needed) is None:
                continue

            for k, v in word.items():
                if counter.get(k) is None:
                    break

                if v > counter.get(k):
                    condition = False
                    break
            else:
                count += 1

        answer_count.append([ch, count])
    answer_count.sort(key=lambda x: (x[1], x[0]))

    min_alpha = ""
    min_value = answer_count[0][1]
    for a, b in answer_count:
        if b == min_value:
            min_alpha += a
        else:
            break

    max_alpha = ""
    max_value = answer_count[-1][1]
    for a, b in answer_count:
        if b == max_value:
            max_alpha += a

    print(min_alpha, min_value, max_alpha, max_value)


