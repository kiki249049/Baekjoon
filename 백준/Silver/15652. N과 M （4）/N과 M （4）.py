import sys
input = sys.stdin.readline

def nCr(n,r,s) :
    if r == 0 :
        print(*comb)
    else :
        for i in range(s,n) :
            comb[M-r]=A[i]
            nCr(n,r-1,i)


N,M = map(int,input().split())
A = [i for i in range(1,N+1)]
comb = [0]*M
nCr(N,M,0)