import sys
input = sys.stdin.readline

def dsearch(n) :
    group=[]
    stack = []
    stack.append(n)
    while stack :
        t = stack.pop()
        visited[t] = 1
        group.append(t)
        for i in range(1,N+1):
            if G[t][i] == 1 and not visited[i] :
                stack.append(i)
    bg_group.append(group)


N,M,C = map(int,input().split())
cost = list(map(int,input().split()))
visited = [0] * (N+1)
G = [[0]*(N+1) for _ in range(N+1)]
cnt = 0
bg_group = []
for i in range(M) :
    v,w = map(int,input().split())
    G[v][w] = 1
    G[w][v] = 1
for i in range(1,N+1) :
    if not visited[i] :
        dsearch(i)
how = 0
for i in bg_group :
    min_val = 10001
    for k in range(len(i)) :
        val = cost[i[k]-1]
        if min_val > val :
            min_val = val
    how += min_val
if 0 in visited[1:] or how > C :
    print("Oh no")
else :
    print(how)