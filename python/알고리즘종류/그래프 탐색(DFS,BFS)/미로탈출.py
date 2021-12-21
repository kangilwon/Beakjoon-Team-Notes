# BFS 소스코드 구현

def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복한다.
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 벗어난 경우 무시한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시한다.
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        # 가장 오른쪽 아래까지의 최단 거리를 반환한다.
        return graph[n - 1][m - 1]


from collections import deque

# n, m 을 공백을 기준으로 입력 받는다.
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력 받는다.
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS를 수행한 결과를 출력한다.