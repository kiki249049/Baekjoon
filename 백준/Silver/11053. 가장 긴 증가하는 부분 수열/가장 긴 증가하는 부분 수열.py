import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1] * N
for i in range(N) :
    for k in range(i) :
        if A[i] > A[k] :
            dp[i] = max(dp[i],dp[k]+1)
print(max(dp))