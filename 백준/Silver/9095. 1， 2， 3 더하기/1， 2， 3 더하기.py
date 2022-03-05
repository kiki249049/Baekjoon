import sys

input=sys.stdin.readline

def bfs(box) :
    global answer
    if sum(box) == n :
        answer += 1
        return
    for i in [1,2,3] :
        if sum(box)+i <= n :
            box.append(i)
            bfs(box)
            box.pop()


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    answer=0
    box=[]
    bfs(box)
    print(answer)