import sys
from collections import deque
input = sys.stdin.readline

def bsearch(start) :
    x,y = start
    chess[x][y] = 1
    go = deque()
    go.append(start)
    while go :
        x,y = go.popleft()
        for dx,dy in [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)] :
            nx,ny = x+dx, y+dy
            if 0<= nx < I and 0<= ny < I :
                if chess[nx][ny] > chess[x][y]+1 :
                    chess[nx][ny] = chess[x][y] + 1
                    go.append((nx,ny))




T = int(input())
for i in range(1,T+1) :
    I = int(input())
    chess=[[100000]*I for _ in range(I)]
    start = tuple(map(int,input().split()))
    destination = tuple(map(int,input().split()))
    bsearch(start)
    print(chess[destination[0]][destination[1]]-1)