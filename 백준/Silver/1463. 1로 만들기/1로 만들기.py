from collections import deque

def bfs(N) :
    queue=deque()
    queue.append(N)
    while queue :
        t=queue.popleft()
        if t==1 :
            return visited[1]
        if t%3 == 0 and not visited[t//3]:
            visited[t//3] = visited[t] + 1
            queue.append(t//3)
        if t%2 == 0 and not visited[t//2]:
            visited[t//2] = visited[t] + 1
            queue.append(t//2)
        if not visited[t-1] :
            visited[t-1] = visited[t] + 1
            queue.append(t-1)



N=int(input())
cnt = 0
visited=[0]*1000001
print(bfs(N))