import sys

input = lambda : sys.stdin.readline().rstrip()
N, P, Q = map(int, input().split())
answer_table = dict()

def solve(r, p, q):
    if r == 0:
        return 1

    if answer_table.get(r) != None:
        return answer_table[r]
    
    answer = solve(r//p, p, q) + solve(r//q, p, q)
    answer_table[r] = answer
    return answer

print(solve(N, P, Q))
