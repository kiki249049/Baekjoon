import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)] # 그래프 정보를 넣어줄 리스트 선언
distance = [INF]*(V+1) # 최단경로 리스트 선언
visited = [False]*(V+1) # 방문표시 리스트 선언
for i in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) # u에서 v로가는 비용이 w다.

def dijkstra(start) :
    q = [] # 힙만들어주기
    distance[start] = 0 # start의 최단경로는 0으로 만들어준다.
    heapq.heappush(q,(0,start)) # 최단경로와 본인의 노드지점의 쌍을 힙에 넣어줌
    while q :
        # 가장 짧은 최단경로의 노드에 대한 정보를 꺼낸다.
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,V+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])