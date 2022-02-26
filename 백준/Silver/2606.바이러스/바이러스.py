def virus(n) :
    stack=[]
    stack.append(n)
    cnt=0
    while stack :
        t=stack.pop()
        if not visited[t] :
            visited[t] = 1
        for i in range(1,len(G[t])) :
            if G[t][i] == 1 and visited[i] == 0 and i not in stack :
                stack.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

V=int(input())
E=int(input())
computers=[]
visited = [0] * (V + 1)
for i in range(E) :
    computers.append(list(map(int,input().split())))
G=[[0]*(V+1) for _ in range(V+1)]
for i in range(E) :
    G[computers[i][0]][computers[i][1]] = 1
    G[computers[i][1]][computers[i][0]] = 1
print(virus(1))