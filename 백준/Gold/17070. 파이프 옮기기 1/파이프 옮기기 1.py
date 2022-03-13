import sys
input = sys.stdin.readline

def dfs(x,y) :
    global ans
    if mat[N-1][N-1] == 1 :
        return
    if mat[x][y-1] == 2 and x != N-1 and y==N-1 :
        return
    if mat[x-1][y] == 2 and x == N-1 and y != N-1 :
        return
    if x==N-1 and y == N-1 :
        ans += 1
        return
    if 0<=x<N and 0<=y-1<N and mat[x][y-1] == 2 : # 가로 방향일 경우
        if 0<=x<N and 0<=y+1<N and mat[x][y+1] == 0  : # 가로로 밈
            mat[x][y+1] = 2
            dfs(x,y+1)
            mat[x][y+1] = 0
        if 0 <= x+1 < N and 0 <= y+1 < N and mat[x+1][y]==0 and mat[x][y+1]==0 and mat[x+1][y+1] == 0: # 가로+대각선
            mat[x+1][y+1] = 2
            dfs(x+1, y+1)
            mat[x+1][y+1] = 0
    elif 0<=x-1<N and 0<=y<N and mat[x-1][y] == 2 : # 세로 방향일 경우
        if 0<=x+1<N and 0<=y<N and mat[x+1][y] == 0  : # 세로로 밈
            mat[x+1][y] = 2
            dfs(x+1,y)
            mat[x+1][y] = 0
        if 0 <= x+1 < N and 0 <= y + 1 < N and  mat[x+1][y]==0 and mat[x][y+1]==0 and mat[x+1][y+1] == 0: # 세로 대각선으로 밈
            mat[x+1][y + 1] = 2
            dfs(x+1, y+1)
            mat[x+1][y + 1] = 0
    elif 0<=x-1<N and 0<=y-1<N and mat[x-1][y-1] == 2 : # 대각선 방향일 경우
        if 0<=x<N and 0<=y+1<N and mat[x][y+1] == 0  :
            mat[x][y+1] = 2
            dfs(x,y+1)
            mat[x][y+1] = 0
        if 0 <= x+1 < N and 0 <= y < N and mat[x+1][y] == 0:
            mat[x+1][y] = 2
            dfs(x+1, y)
            mat[x+1][y] = 0
        if 0 <= x+1 < N and 0 <= y + 1 < N and  mat[x+1][y]==0 and mat[x][y+1]==0 and mat[x+1][y+1] == 0:
            mat[x+1][y + 1] = 2
            dfs(x+1, y + 1)
            mat[x+1][y + 1] = 0
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
mat[0][0]=2
mat[0][1]=2
ans = 0
dfs(0,1)
print(ans)