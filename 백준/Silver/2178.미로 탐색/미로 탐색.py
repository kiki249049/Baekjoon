def maze_min(x,y) :
    queue=[]
    visited=[[0]*M for _ in range(N)]
    queue.append([x,y])
    while queue :
        i,j=queue.pop(0)
        if i == N-1 and j == M-1 :
            return visited[i][j]
        if not visited[i][j] :
            visited[i][j] = 1
        for di,dj in [[0,-1],[1,0],[0,1],[-1,0]] :
            ni, nj = i+di,j+dj
            if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0 and maze[ni][nj] == 1 :
                queue.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1
    return 0

N,M=map(int,input().split())
maze=[list(map(int,input())) for _ in range(N)]
print(maze_min(0,0))
