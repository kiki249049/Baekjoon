import sys


T=int(input())
array=[]
for i in range(T) :
    array.append(list(map(int,sys.stdin.readline().split())))
array.sort()
for i in array :
    print(*i)