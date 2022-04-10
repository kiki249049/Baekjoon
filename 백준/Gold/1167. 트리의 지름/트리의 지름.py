import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def search(n,val) : # 최대노드를 찾는 함수
    global temp,y
    if n :
        if len(child[n])>=1 :
            for i in child[n] :
                search(i[0],val+i[1])
        else :
            if val > temp :
                temp = val
                y = n
            return

def inv_search(n,val) : # 부모 노드가 들어옴
    global temp, y, real_left,ans
    if len(child[n])>= 1:
        for i in child[n]:
            if i[0] != pre:  # 전 노드와 다르다면
                inv_search(i[0], val + i[1])
            elif i[0] == pre and len(child[n]) == 1 :
                ans = max(left+val,ans)
    else:
        ans = max(ans,left+val)
        return
def find_parent(x) :
    if x != parent[x] :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b) :
    a = find_parent(a)
    b = find_parent(b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a
def find_child(n) : # bfs로 자식찾기
    queue = deque()
    visited[n] = 1
    queue.append(n)
    while queue :
        t = queue.popleft() # 하나씩 빼서
        for i in con[t] :
            if not visited[i[0]] :
                visited[i[0]] = visited[t]+1
                queue.append(i[0])

V = int(input())
con=[[] for _ in range(V+1)]
parent=[x for x in range(V+1)]
visited=[0] * (V+1)
child = [[] for _ in range(V+1)]
p = [[] for _ in range(V+1)]
ans = 0
y = 0
temp = 0
for i in range(V) :
    line = list(map(int,input().split()))
    j = 1
    while line[j] != -1 :
        con[line[0]].append((line[j],line[j+1]))
        j += 2
for i in range(V) :
    for j in con[i] :
        if find_parent(i) != find_parent(j[0]) :
            union(i,j[0])
for i in range(V) :
    find_parent(i)
start = parent[1]
find_child(start)
for i in range(1,V+1) :
    for j in con[i] :
        if visited[i] < visited[j[0]] :
            child[i].append(j)
            p[j[0]].append((i,j[1]))
search(1,0)
temp = 0
pre = y
node = p[y][0][0]
left = 0
real_left =  p[y][0][1]
while True: # 루트가 아닐동안
    left += p[pre][0][1]
    inv_search(node,0) # 역추적
    pre = node # 전 노드 기억
    if node == 1 :
        break
    node = p[node][0][0] # 노드변환
print(ans)
