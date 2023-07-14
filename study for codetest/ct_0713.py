############ 시간 초과 에러 해결 ################################
# import sys
# input = sys.stdin.readline
# n = int(input())

# for i in range(n):
#     a,b = map(int, input().split())
#     for j in range(b):
#           c,d = map(int, input().split())
#     print(a-1)
    
    
    
    
    


### 트리 정리 ###
# 트리는 그래프의 한 종류
# 1. 사이클이 없어야 함(한 노드에서 출발하여 다시 같은 노드로 돌아오는 경로 없어야 함)
# 2. 연결되어 있어야 함
# 3. 간선의 수가 노드의 수에서 1 뺀 값이어야 함
################

# x,y 간 연결되면서 대표 노드 값으로 변경
# parents = [0,1,2,3,4,5] 일 경우, 0번째와 1번째가 연결되면 대표 노드값으로 변경
# => [0,0,2,3,4,5]

# import sys
# input = sys.stdin.readline

# def union(x,y):
#     x = find(x)
#     y = find(y)
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y

# # 재귀 사용해 대표 노드를 찾아감
# def find(x):
#     if x != parents[x]:
#         parents[x] = find(parents[x])
#     return parents[x]

# idx = 0
# while True:
#     idx += 1
#     n,m = map(int,input().split())
#     if n==0 and m==0:
#         break
#     parents = [i for i in range(n+1)]
#     cycle = set()
#     for _ in range(m):
#         a,b = map(int,input().split())
#         if find(a) == find(b):
#             cycle.add(parents[a])
#             cycle.add(parents[b])
#         # 두 정점 중 하나가 사이클에 포함되는 정점이라면 나머지 정점도 사이클로 포함.
#         if parents[a] in cycle or parents[b] in cycle: 
#             cycle.add(parents[a])
#             cycle.add(parents[b])
#         union(a,b)
    
#     for i in range(n+1):
#         find(i)
    
#     parents = set(parents)
#     answer = sum([1 if i not in cycle else 0 for i in parents])-1
#     if answer == 0:
#         print(f'Case {idx}: No trees.')
#     elif answer == 1:
#         print(f'Case {idx}: There is one tree.')
#     else:
#         print(f'Case {idx}: A forest of {answer} trees.')




# 동적 계획법

# n = int(input())
# costs = []
# for _ in range(n):
#     costs.append(list(map(int, input().split())))

# dp = [[0]*3 for _ in range(n)]  # 각 집에 대해 RGB 각 색깔로 칠하는 최소 비용을 저장할 dp 테이블 생성
# dp[0] = costs[0]  # 첫번째 집을 칠하는 비용 초기화
# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # 현재 집을 빨간색으로 칠하는 경우, 이전 집은 초록색 또는 파란색이어야 함
#     dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # 현재 집을 초록색으로 칠하는 경우, 이전 집은 빨간색 또는 파란색이어야 함
#     dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

# print(min(dp[-1]))

def fibonacci(n):
    fib = [0, 1] + [0] * (n-1)  # n까지의 피보나치 수를 저장할 리스트를 초기화합니다.
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]  # 각 피보나치 수를 계산하고 저장합니다.
    return fib[n]  # 원하는 피보나치 수를 반환합니다.

print(fibonacci(10))  # 10번째 피보나치 수를 출력합니다.






a, b = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(a)]
B = [list(map(int, list(input()))) for _ in range(a)]
cnt = 0

def flip(x, y, A):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]
            
for i in range(0, a-2):
    for j in range(0, b-2):
        if A[i][j] != B[i][j]:
            flip(i,j,A)
            cnt +=1
if A !=B:
    print(-1)
else:
    print(cnt)
    