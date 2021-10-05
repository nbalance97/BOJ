import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

member_dict = {}
team_dict = {}

for _ in range(N):
    team = input()
    team_dict[team] = []
    member_count = int(input())
    for __ in range(member_count):
        member = input()
        team_dict[team].append(member)
        member_dict[member] = team

    team_dict[team] = sorted(team_dict[team])

for _ in range(M):
    question = input()
    question_type = int(input())
    if question_type == 0:
        for m in team_dict[question]:
            print(m)
    elif question_type == 1:
        print(member_dict[question])
