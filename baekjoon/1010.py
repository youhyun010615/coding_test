import sys

input = sys.stdin.readline

def comb(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N))