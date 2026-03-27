import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited_order = [0] * (N + 1)
q = deque([R])
order = 1
visited_order[R] = order

while q:
    now = q.popleft()
    for nxt in graph[now]:
        if visited_order[nxt] == 0:
            order += 1
            visited_order[nxt] = order
            q.append(nxt)

for i in range(1, N + 1):
    print(visited_order[i])