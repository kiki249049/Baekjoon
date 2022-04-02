A = input()
N = len(A)
B = input()
M = len(B)
memo = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1) :
    for k in range(1,M+1) :
        if A[i-1] != B[k-1] :
            memo[i][k] = max(memo[i-1][k],memo[i][k-1])
        else :
            memo[i][k] = memo[i-1][k-1]+1
print(memo[len(A)][len(B)])
