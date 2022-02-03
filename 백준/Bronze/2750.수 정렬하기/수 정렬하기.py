import sys


T=int(input())
answer=[]
for i in range(T) :
    answer.append(int(sys.stdin.readline().rstrip()))
answer.sort()
for i in answer :
    print(i)