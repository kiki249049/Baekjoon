import sys

input=sys.stdin.readline

N=int(input())
times=list(map(int,input().split()))
times.sort()
answer=0
for i in range(N) :
    for k in range(i+1) :
        answer += times[k]
print(answer)