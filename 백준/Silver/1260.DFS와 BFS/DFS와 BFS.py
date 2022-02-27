def dfs(n) :
    stack=[]
    stack.append(n)
    while stack :
        t=stack.pop()
        if not visited[t] :
            visited[t] = 1
            dfs_answer.append(t)
        for i in range(len(G[t])-1,0,-1) :
            if G[t][i] == 1 and visited[i] == 0 :
                stack.append(i)

def bfs(n) :
    queue=[]
    queue.append(n)
    while queue :
        t=queue.pop(0)
        if not visited[t] :
            visited[t] = 1
            bfs_answer.append(t)
        for i in range(1,len(G[t])) :
            if G[t][i] == 1 and visited[i] == 0 :
                queue.append(i)





V,E,n = map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(E)]
G=[[0]*(V+1) for _ in range(V+1)]
visited=[0]*(V+1)
dfs_answer=[]
bfs_answer=[]
for i in range(E) :
    G[mat[i][0]][mat[i][1]] = 1
    G[mat[i][1]][mat[i][0]] = 1
dfs(n)
visited=[0]*(V+1)
bfs(n)
print(*dfs_answer)
print(*bfs_answer)
