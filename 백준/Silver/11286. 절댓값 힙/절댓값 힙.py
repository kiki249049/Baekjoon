import sys
import heapq
input = sys.stdin.readline


N = int(input())
q=[]
for i in range(N) :
    order = int(input())
    if order != 0 : # 0 아니면 넣고
        heapq.heappush(q,(abs(order),order))
    else : # 0 이면
        if len(q) == 0 :
            print(0)
        else :
            print(heapq.heappop(q)[1])
