N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
dp0=[0]*N
dp0[0] = cost[0][0]
dp1=[0]*N
dp1[0] = cost[0][1]
dp2=[0]*N
dp2[0] = cost[0][2]
for i in range(1,N) :
    dp0[i] += cost[i][0]+min(dp1[i-1],dp2[i-1])
    dp1[i] += cost[i][1]+min(dp2[i-1],dp0[i-1])
    dp2[i] += cost[i][2]+min(dp0[i-1],dp1[i-1])
print(min(dp0[N-1],dp1[N-1],dp2[N-1]))