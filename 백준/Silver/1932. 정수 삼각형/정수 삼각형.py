import sys
input = sys.stdin.readline

N = int(input())
area = []
dp = []
for i in range(N) :
    area.append(list(map(int,input().split())))
for i in range(1,N+1) :
    dp.append([0]*i)
dp[0][0] = area[0][0]
for i in range(1,N) :
    for k in range(i+1):
        if k == 0 :
            dp[i][k] = area[i][k]+dp[i-1][k]
        elif k == i :
            dp[i][k] = area[i][k]+dp[i-1][k-1]
        else :
            dp[i][k] = area[i][k]+max(dp[i-1][k],dp[i-1][k-1])
print(max(dp[N-1]))