import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 제한을 늘려 런타임 에러 방지

N, M = map(int, input().split()) # 정점 개수 N, 간선 개수 M

graph = [[] for _ in range(N + 1)] # 각 정점과 연결된 정점들을 저장할 리스트

for _ in range(M): # 간선 정보 입력받아 양방향으로 저장
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1) # 방문 여부를 저장하는 리스트

def dfs(x):
    visited[x] = True # 현재 정점 방문 처리

    for nxt in graph[x]:  # 현재 정점과 연결된 정점들 중 아직 방문하지 않은 정점 계속 탐색
        if not visited[nxt]:
            dfs(nxt)

count = 0

for i in range(1, N + 1): # 아직 방문하지 않은 정점이 나오면 새로운 연결 요소 시작
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
