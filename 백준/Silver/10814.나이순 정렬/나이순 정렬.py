import sys

N=int(input())

people=[sys.stdin.readline().split() for i in range(N)]
box=[[] for i in range(201)]
for i in people :
    box[int(i[0])] += [i]
for i in range(len(box)) :
    for k in range(len(box[i])) :
        print(*box[i][k])
