import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

def determine(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime = []
for i in range(2, 150):
    if determine(i):
        prime.append(i)

prime_multiple = set()
for i in range(1, len(prime)):
    prime_multiple.add(prime[i] * prime[i-1])

while True:
    N = N + 1
    if N in prime_multiple:
        break

print(N)

    
