import sys
from collections import Counter


input = lambda: sys.stdin.readline().rstrip()
N = int(input())

books = [input() for _ in range(N)]
counter = Counter(books)
max_sell_count = max(counter.values())

answer = sorted([name for name, v in counter.items() if v == max_sell_count])[0]
print(answer)
