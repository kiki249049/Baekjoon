import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dont_hear=set()
dont_see=set()
answer=[]
for i in range(N) :
    dont_hear.add(input().rstrip())
for i in range(M) :
    dont_see.add(input().rstrip())
answer=list(dont_see&dont_hear)
answer.sort()
print(len(answer))
for i in answer:
    print(i)