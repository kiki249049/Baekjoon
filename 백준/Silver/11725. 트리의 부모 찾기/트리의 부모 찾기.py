import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def search(n) :
    if not visited[n] :
        visited[n] = 1
        seq.append(n)
        for i in range(len(node[n])) :
            if node[n][i] == p[n] :
                continue
            p[node[n][i]] = n
            search(node[n][i])

N = int(input())
node = [[] for _ in range(N+1)]
visited = [False]*(N+1)
seq = []
p = [0]*(N+1)
for i in range(N-1) :
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
search(1)
for i in range(2,N+1):
    print(p[i])