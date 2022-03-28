import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
numbers=[]
for i in range(1,N+1):
    numbers.append(i)
com = list(combinations(numbers,M))
for i in com :
    print(*i)