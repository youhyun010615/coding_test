from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))
answer = 0

for target in targets:
    while True:
        if dq[0] == target:
            dq.popleft()
            break

        idx = dq.index(target)

        if idx <= len(dq) // 2:
            dq.append(dq.popleft())   
            answer += 1
        else:
            dq.appendleft(dq.pop())   
            answer += 1

print(answer)