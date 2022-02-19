import sys

box=[0]*10001
N=int(input())
for i in range(N) :
    box[int(sys.stdin.readline().rstrip())] += 1
for i in range(len(box)) :
    for k in range(box[i]) :
        print(i)
