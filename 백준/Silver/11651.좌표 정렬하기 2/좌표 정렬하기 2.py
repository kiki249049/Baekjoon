import sys

N=int(sys.stdin.readline())
box=[]
for i in range(N) :
    box.append(list(map(int,sys.stdin.readline().split())))
for i in box :
    i.reverse()
box.sort()
for i in box :
    i.reverse()
for i in box :
    print(*i)