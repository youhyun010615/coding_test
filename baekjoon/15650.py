import sys
input = sys.stdin.readline

def backtrack(start, path):
  if len(path) == M :
    print(' '.join(map(str, path)))
    return
  
  for i in range(start, N + 1):
    path.append(i)
    backtrack(i + 1, path)
    path.pop()

N, M = map(int, input().split())
backtrack(1, [])