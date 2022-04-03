import sys
from copy import deepcopy
input = sys.stdin.readline

def nPr(n,r,s) :
    if r == s :
        hi = deepcopy(p)
        hi = tuple(hi)
        if tuple(p) in ans :
            return
        else :
            print(*p)
            ans.add(hi)
            return
    else :
        for i in range(N) :
            if not used[i] :
                used[i] = 1
                p[s] = number[i]
                nPr(n,r,s+1)
                used[i] = 0
N,M = map(int,input().split())
number = list(map(int,input().split()))
used = [0]*N
p = [0]*M
number.sort()
ans = set()
nPr(N,M,0)