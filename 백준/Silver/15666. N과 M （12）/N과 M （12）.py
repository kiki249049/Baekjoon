import sys
from copy import deepcopy
input = sys.stdin.readline

def dfs(dep,idx) :
    if dep == M :
        hi = deepcopy(temp)
        hi.sort()
        if tuple(hi) not in ans :
            hi = tuple(hi)
            ans.add(hi)
            print(*hi)
        else :
            return
    else :
        for i in range(idx,N) :
            temp.append(number[i])
            dfs(dep+1,i)
            temp.pop()
N,M = map(int,input().split())
number = list(map(int,input().split()))
temp = []
number.sort()
ans = set()
dfs(0,0)