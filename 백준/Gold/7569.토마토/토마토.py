from collections import deque
import sys

def ripe(start) :
    global day
    queue=deque()
    for i in start :
        queue.append(i)
    while queue :
        z,x,y = queue.popleft()
        for dz,dx,dy in [[0,-1,0],[0,0,-1],[0,1,0],[0,0,1],[1,0,0],[-1,0,0]] :
            nz = z + dz
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomatoes[nz][nx][ny] == 0 :
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                queue.append([nz,nx,ny])
                day=tomatoes[nz][nx][ny]


M,N,H=map(int,sys.stdin.readline().split())
tomatoes=[]
start=[]
day=0
out = 0
for i in range(H) :
    tomatoes.append([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
for i in range(H) :
    for k in range(N):
        for j in range(M) :
            if tomatoes[i][k][j] == 1 :
                start.append([i,k,j])
ripe(start)
for i in range(H) :
    for k in range(N):
        for j in range(M) :
            if tomatoes[i][k][j] == 0 :
                out += 1
                print(-1)
                break
        if tomatoes[i][k][j] == 0:
            break
    if tomatoes[i][k][j] == 0:
        break
if out==0 and day==0 :
    print(day)
elif out == 0 :
    print(day-1)