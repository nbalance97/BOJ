import sys

input = lambda: sys.stdin.readline().rstrip()

tc_count = int(input())
for step in range(tc_count):
    print("Scenario #%d:"%(step+1))
    word_count = int(input())
    words = [input() for _ in range(word_count)]
    people_count = int(input())
    for _ in range(people_count):
        question = list(map(int, input().split()))
        question = question[1:]
        string = "".join(map(lambda x:words[x], question))
        print(string)
    if step != tc_count-1:
        print()

