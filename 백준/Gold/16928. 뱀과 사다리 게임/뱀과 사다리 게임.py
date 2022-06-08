import sys
from collections import deque
input = sys.stdin.readline

def bsearch(depart) :
    deq = deque()
    area[depart] = 0
    deq.append(depart)
    while deq :
        here = deq.popleft()
        for i in range(1,7):
            if here+i <= 100 :
                next = teleport[here+i]
                if area[next] > area[here]+1 :
                    area[next] = area[here]+1
                    deq.append(next)




N,M = map(int,input().split())
area=[1000000]*101
teleport=[i for i in range(101)]
ans = int(1e9)
for i in range(N+M) : # 사다리 정보
    start, arrive = map(int,input().split())
    teleport[start] = arrive
bsearch(1)
print(area[100])

