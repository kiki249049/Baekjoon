import sys


N=int(sys.stdin.readline())
scores=[0]
for i in range(N) :
    scores.append(int(sys.stdin.readline()))
arr=[0]*(N+1)
if N == 1:
    arr[1] = scores[1]
if N == 2:
    arr[2] = scores[1] + scores[2]
if N==3 :
    arr[3] = max(scores[1] + scores[3], scores[2] + scores[3])
if N>=4:
    for i in range(4,N+1):
        arr[1] = scores[1]
        arr[2] = scores[1] + scores[2]
        arr[3] = max(scores[1] + scores[3], scores[2] + scores[3])
        arr[i]=max(scores[i]+scores[i-1]+arr[i-3],scores[i]+arr[i-2])
print(arr.pop())