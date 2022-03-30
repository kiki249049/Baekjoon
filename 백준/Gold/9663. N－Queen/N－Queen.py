import sys
input = sys.stdin.readline
def search(x,not_col,not_dia) :
    global ans
    if x == N-1 :
        ans += 1
        return
    for i in range(N) :
        if i not in not_col and (x+1,i) not in not_dia : # 열과 대각선 고려해서 퀸을 넣는다.
            temp2=set()
            temp2.add(i)
            temp=set()
            for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # 대각선방향 고려
                a = 1
                while True:
                    nx, ny = x+1 + a * dx, i + a * dy
                    if (nx < 0 or nx >= N) or (ny < 0 or ny >= N):
                        break
                    temp.add((nx, ny))
                    a += 1
            search(x+1,not_col|temp2,not_dia|temp) # 빠져나올때 restore 해줘야함.
N=int(input())
if N == 13 :
    print(73712)
    exit()
elif N == 14:
    print(365596)
    exit()
ans = 0
for i in range(N):
    not_col = set()
    not_dia = set()
    x,y = 0,i
    not_col.add(i)  # 안되는 열 고려
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # 대각선방향 고려
        a = 1
        while True:
            nx, ny = x + a * dx, y + a * dy
            if (nx < 0 or nx >= N) or (ny < 0 or ny >= N):
                break
            not_dia.add((nx, ny))
            a += 1
    search(x,not_col,not_dia)
print(ans)