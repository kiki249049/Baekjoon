import sys
input = sys.stdin.readline

def search(lev) :
    if lev == M :
        print(*ans)
        return
    for i in range(1,N+1) :
        ans.append(numbers[i])
        search(lev+1)
        ans.pop()



N,M = map(int,input().split())
numbers = [i for i in range(N+1)]
ans = []
search(0)