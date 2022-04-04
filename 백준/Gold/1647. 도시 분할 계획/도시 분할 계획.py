import heapq
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
ans = 0
cnt = 0
cancer = 0
for i in range(M) :
    A,B,C = map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

q = []
heapq.heappush(q,(0,1)) # 1번부터 시작하고 가중치 0
while cnt < N :
    C,A = heapq.heappop(q)
    if visited[A] :
        continue
    visited[A] = True
    cancer = max(cancer,C)
    ans += C
    cnt += 1
    for i in graph[A] :
        heapq.heappush(q,i)
print(ans-cancer)