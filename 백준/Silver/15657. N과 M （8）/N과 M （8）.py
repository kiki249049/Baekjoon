import sys
input = sys.stdin.readline

def dfs(s) :
    if len(temp) == M :
        print(*temp)
    else :
        for i in range(s,N) :
            temp.append(number[i])
            dfs(i)
            temp.pop()

N,M = map(int,input().split())
number = list(map(int,input().split()))
temp = []
number.sort()
ans = []
dfs(0)