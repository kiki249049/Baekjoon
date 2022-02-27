import sys
from collections import deque

def find_veg(x,y) :
    queue = deque()
    area[x][y] = 2
    queue.append([x,y])
    while queue :
        p,q = queue.popleft()
        for dp,dq in [[-1,0],[0,-1],[1,0],[0,1]] :
            np = p + dp
            nq = q + dq
            if 0<= np < M and 0<= nq < N and area[np][nq] == 1 :
                queue.append([np,nq])
                area[np][nq] = 2


T=int(sys.stdin.readline())
for tc in range(1,T+1):
    M,N,K = map(int,sys.stdin.readline().split())
    cnt=0
    area=[[0]*N for _ in range(M)]
    for i in range(K):
        x,y = map(int,sys.stdin.readline().split())
        area[x][y] = 1
    for i in range(M):
        for k in range(N) :
            if area[i][k] == 1 :
                find_veg(i,k)
                cnt +=1
    print(cnt)