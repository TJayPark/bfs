from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  que = deque()
  que.append((x,y))
  while que:
    x, y = que.popleft()

    for ddx, ddy in zip(dx, dy):
      newX = x + ddx
      newY = y + ddy
      if(newX < 0 or newX >= N or newY < 0 or newY >= M):
        continue
      if(graph[newX][newY]==0):
        continue
      if(graph[newX][newY]==1):
        graph[newX][newY] = graph[x][y] + 1
        que.append((newX,newY))

  return graph[N-1][M-1]
  
print(bfs(0,0))
    