import sys
from collections import deque

input=sys.stdin.readline

def dfs(n) :
    global answer
    queue=deque()
    queue.append(n)
    while queue :
        t=queue.popleft()
        for i in range(1,V+1) :
            if G[t][i]==1 and not visited[i] :
                visited[i]=1
                queue.append(i)
    answer += 1
    return


V,E=map(int,input().split())
node=[]
answer=0
visited = [0] * (V + 1)
G=[[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    node.append(list(map(int,input().split())))
for i in range(E) :
    G[node[i][0]][node[i][1]]=1
    G[node[i][1]][node[i][0]]=1
for i in range(1,V+1) :
    if not visited[i]:
        dfs(i)
print(answer)