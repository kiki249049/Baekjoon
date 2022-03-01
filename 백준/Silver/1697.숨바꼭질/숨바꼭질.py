from collections import deque

def bfs() :
    queue=deque()
    queue.append(N)
    while queue :
        t=queue.popleft()
        if t==K :
            print(visited[t])
            break
        for i in [t-1,t+1,2*t]:
            if 0<=i<=100000 and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1







N,K=map(int,input().split())
visited=[0] * 100001
bfs()