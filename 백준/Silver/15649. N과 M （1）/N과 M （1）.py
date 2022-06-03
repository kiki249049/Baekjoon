import sys
input = sys.stdin.readline

def search(lev) :
    if lev == M :
        print(*ans)
        return
    for i in range(1,N+1) :
        if not used[i] :
            used[i] = 1
            ans.append(numbers[i])
            search(lev+1)
            ans.pop()
            used[i]=0



N,M = map(int,input().split())
numbers = [i for i in range(N+1)]
used = [0]*(N+1)
ans = []
search(0)