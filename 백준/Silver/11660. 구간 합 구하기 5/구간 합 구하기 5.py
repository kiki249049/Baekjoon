import sys
input = sys.stdin.readline

N,M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
cal = [item[:] for item in area]
for x in range(N) :
    for y in range(N) :
        for dx,dy in [(-1,0),(0,-1),(-1,-1)] :
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and (dx==0 or dy==0) :
                cal[x][y] += cal[nx][ny]
            elif 0<=nx<N and 0<=ny<N :
                cal[x][y] -= cal[nx][ny]
for i in range(M) :
    x1,y1,x2,y2 = map(int,input().split())
    temp = cal[x2-1][y2-1]
    if 0<=x1-2<N and 0<=y1-2<N :
        temp += cal[x1-2][y1-2]
    if 0<=x2-1<N and 0<=y1-2<N :
        temp -= cal[x2-1][y1-2]
    if 0<=x1-2<N and 0<=y2-1<N :
        temp -= cal[x1-2][y2-1]
    print(temp)