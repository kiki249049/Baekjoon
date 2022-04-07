import sys
from copy import deepcopy
input = sys.stdin.readline

N,K = map(int,input().split())
stuff = []
for i in range(N) :  # 가치를 크게하는게 목표, 중복이 쓰이면 안됨.
    w,v = map(int,input().split())
    stuff.append((w,v))
op = [0] * (K+1)
memo = [[x for x in range(N)] for _ in range(K+1)]
w = 1
while w <= K :
    for i in range(N) :
        if w-stuff[i][0] >= 0 :
            try:
                if op[w-stuff[i][0]]+stuff[i][1] > op[w] :
                    if len(memo[w-stuff[i][0]]) == 0 :
                        op[w] = op[w-stuff[i][0]]
                        memo[w] = deepcopy(memo[w-stuff[i][0]])
                        continue
                    memo[w-stuff[i][0]].remove(i)
                    op[w] = op[w-stuff[i][0]]+stuff[i][1]
                    memo[w] = deepcopy(memo[w-stuff[i][0]])
                    memo[w-stuff[i][0]].append(i)
            except :
                continue
    w += 1
print(max(op))