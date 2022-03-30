import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy

def diffusion() :
    queue = deque()
    for i in range(N):
        for k in range(M):
            if vir[i][k] == 2: # 시작바이러스
                queue.append((i,k))
    while queue :
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)] :
            nx,ny =x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and not vir[nx][ny] :
                vir[nx][ny] = 2


N,M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
ans = 0
box = []
for i in range(N) :
    for k in range(M) :
        if not area[i][k] :
            box.append((i,k))
for C in combinations(box,3):
    vir=deepcopy(area) # 가상 한세트
    for j in C :
        x,y = j
        vir[x][y] = 1
    for p in range(2*N) :
        diffusion()
    val = 0
    for i in range(N):
        for k in range(M):
            if vir[i][k] == 0 :
                val += 1
    ans = max(ans,val)
print(ans)