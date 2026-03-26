from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = [0] * (n + 1)
queue = deque([r])
visited[r] = 1
order = 2

while queue:
    now = queue.popleft()

    for nxt in graph[now]:
        if visited[nxt] == 0:
            visited[nxt] = order
            order += 1
            queue.append(nxt)

for i in range(1, n + 1):
    print(visited[i])