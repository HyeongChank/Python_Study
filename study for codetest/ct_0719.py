# a,b = map(int, input().split())

# doublelist = []
# for i in range(8):
#     row = []
#     for j in range(8):
#         if(i+j) % 2 ==0:
#             row.append('B')
#         else:
#             row.append('W')
#     doublelist.append(row)

# doublelist2 = []
# for i in range(8):
#     row = []
#     for j in range(8):
#         if(i+j) % 2 ==0:
#             row.append('W')
#         else:
#             row.append('B')
#     doublelist2.append(row)

# inputdoublelist = []
# for z in range(a):
#     inputrow = list(input())
#     inputdoublelist.append(inputrow)

# countlessAlist = []
# countlessBlist = []
# def calcul(inputarray):
#     global doublelist
#     global doublelist2
#     global countlessAlist
#     global countlessBlist
#     # print(len(doublelist))
#     # print(len(doublelist[0]))
#     # print(len(doublelist2))
#     # print(len(doublelist2[0]))
#     # print(len(inputarray))
#     # print(len(inputarray[0]))
#     countlessA = 0
#     countlessB = 0
#     for i in range(8):
#         for j in range(8):
#             if doublelist[i][j] != inputarray[i][j]:
#                 countlessA +=1
#             if doublelist2[i][j] != inputarray[i][j]:
#                 countlessB +=1    
#     countlessAlist.append(countlessA)
#     countlessBlist.append(countlessB)
    

# for i in range(a-7):
#     for j in range(b-7):
#         inputarray = [row[j:j+8] for row in inputdoublelist[i:i+8]]

#         calcul(inputarray)

# mina = min(countlessAlist)
# minb = min(countlessBlist)
# result = min(mina, minb)
# print(result)


# vlist = [[1,2],[2,3]]
# vlist.remove([2,3])
# print(vlist)



# n = int(input())
# def operate():
#     for i in range(len(caselist)):
#         for j in range(2):
# for c in range(n):
#     a,b,c = map(int, input().split())

#     caselist = []
#     for i in range(c):
#         x,y = map(int, input().split())
#         caselist.append([x,y])
#     print(caselist)
#     for j in range(c):
#         lx, ly = caselist[j]
#         if operate()==True:
#             count +=1
            
            
            
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, field, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= len(field) or ny < 0 or ny >= len(field[0]):
                continue

            if field[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

def solve():
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    worms = 0
    for i in range(N):
        for j in range(M):
            # field 에서 0,1 주고 visited true, false를 따로 또 조건을 걸어서 문제 해결
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j, field, visited)
                worms += 1

    print(worms)

T = int(input())
for _ in range(T):
    solve()
