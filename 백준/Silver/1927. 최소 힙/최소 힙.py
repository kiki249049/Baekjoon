import sys
import heapq
input = sys.stdin.readline


N=int(input())
h=[]
for i in range(N) :
    val = int(input())
    if val != 0 :
        heapq.heappush(h,val)
    else :
        if len(h) == 0 :
            print(0)
        else :
            print(heapq.heappop(h))