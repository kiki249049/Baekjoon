import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
edges = [[] for _ in range(V+1)]
visited=[False]*(V+1)
cnt = 0
ans = 0
for i in range(E) :
    A,B,C = map(int,input().split())
    edges[A].append((C,B))
    edges[B].append((C,A))
q = []
heapq.heappush(q,(0,1))
while cnt < V :
    C,A = heapq.heappop(q)
    if visited[A] :
        continue
    visited[A] = True
    cnt += 1
    ans += C
    for edge in edges[A] :
        heapq.heappush(q,edge)
print(ans)