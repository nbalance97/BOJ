import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
people = [1 for i in range(n+1)]

parent = [i for i in range(n+1)]


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]


def union(a1, a2):
    one_parent = find(a1)
    another_parent = find(a2)

    if one_parent != another_parent:
        parent[one_parent] = another_parent

        people[one_parent] += people[another_parent]
        people[another_parent] = people[one_parent]

        candies[one_parent] += candies[another_parent]
        candies[another_parent] = candies[one_parent]


for _ in range(m):
    one, another = map(int, input().split())
    union(one, another)

candies_set = []
visited = set()
for i in range(1, n+1):
    p = find(i)
    if p not in visited:
        visited.add(p)
        candies_set.append([people[p], candies[p]])


dp = [0] * k
for p, c in candies_set:
    for i in range(k-1, p-1, -1):
        dp[i] = max(dp[i], dp[i-p] + c)


print(dp[k-1])

