from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j,field, visited):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if nx <0 or nx >= len(field) or ny < 0 or ny >= len(field[0]):
                continue
            if field[nx][ny] ==1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] =True

def solve():
    M, N, K = map(int, input().split())
    field  = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for i in range(K):
        y, x = map(int, input().split())
        field[x][y]=1
    worms = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] ==1 and not visited[i][j]:
                bfs(i,j,field, visited)
                worms +=1
    print(worms)
    
n = int(input())
for i in range(n):
    solve()
                 