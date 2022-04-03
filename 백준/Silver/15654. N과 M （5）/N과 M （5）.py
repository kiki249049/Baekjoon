import sys
from itertools import permutations

N,M = map(int,input().split())
number = list(map(int,input().split()))
ans = []
for P in permutations(number,M) :
    ans.append(P)
ans.sort()
for i in ans :
    print(*i)