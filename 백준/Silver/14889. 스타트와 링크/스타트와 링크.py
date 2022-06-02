import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
total = set(range(N))
ans = int(1e9)
teams = []
for A in combinations(total,N//2) :
    B = list(total-set(A))
    val1 = 0
    val2 = 0
    for idx_a in range(N//2) :
        for idx_b in range(idx_a+1,N//2) :
            val1 += mat[A[idx_a]][A[idx_b]]+mat[A[idx_b]][A[idx_a]]
            val2 += mat[B[idx_a]][B[idx_b]]+mat[B[idx_b]][B[idx_a]]
    ans = min(ans,abs(val1-val2))
print(ans)
