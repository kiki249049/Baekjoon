import sys
from collections import deque

def ripe(tomatos):
    global day
    queue=deque()
    for i in tomatos :
        queue.append(i)
    while queue :
        p,q = queue.popleft()
        for dp,dq in [[-1,0],[0,-1],[1,0],[0,1]] :
            np, nq = p+dp,q+dq
            if 0<=np<N and 0<=nq<M and area[np][nq]==0 :
                area[np][nq] = area[p][q] + 1
                queue.append([np,nq])
                day = area[np][nq]



M,N = map(int,sys.stdin.readline().split())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
start=[]
day=0
out = 0
for i in range(N) :
    for k in range(M) :
        if area[i][k] == 1 :
            start.append([i,k])
ripe(start)
for i in range(N) :
    for k in range(M) :
        if area[i][k] == 0 :
            print(-1)
            out = -1
            break
    if area[i][k] == 0:
        break
if out==0 and day == 0 :
    print(0)
elif out != -1 :
    print(day-1)