from collections import deque

N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점

graph = [[] for _ in range(N + 1)] # 각 정점과 연결된 정점들을 저장할 리스트

for _ in range(M): # 간선 정보 입력받아 양방향으로 저장
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1): # 방문할 수 있는 정점이 여러 개면 번호가 작은 것을 먼저 방문해야 하므로 정렬
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True # 현재 정점 방문 처리
    print(v, end=' ') # 방문한 정점 출력

    for nxt in graph[v]: # 현재 정점과 연결된 정점들 중 아직 방문하지 않은 곳 탐색
        if not visited[nxt]:
            dfs(nxt, visited)

def bfs(v):
    visited = [False] * (N + 1) # BFS용 방문 리스트
    q = deque([v]) # 시작 정점을 큐에 넣고 시작
    visited[v] = True

    while q:
        x = q.popleft() # 큐의 맨 앞 정점 꺼내기
        print(x, end=' ') # 방문한 정점 출력

        for nxt in graph[x]: # 현재 정점과 연결된 정점들 중 아직 방문하지 않은 곳을 큐에 넣음
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False] * (N + 1) # DFS용 방문 리스트
dfs(V, visited)
print()
bfs(V)
