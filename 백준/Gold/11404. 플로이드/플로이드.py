import sys
import heapq
input = sys.stdin.readline

def dikjstra(start) :
    q=[]
    distance[start][start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[start][now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[start][i[0]] :
                distance[start][i[0]] = cost
                heapq.heappush(q,(cost,i[0]))




n = int(input())
m = int(input())
INF = int(1e9)
distance = [[INF] * (n+1) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for i in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
for i in range(1,n+1) :
    dikjstra(i)
distance=distance[1:]
for i in range(n):
    for k in range(n+1) :
        if distance[i][k] == INF :
            distance[i][k] = 0
for i in distance :
    print(*i[1:])