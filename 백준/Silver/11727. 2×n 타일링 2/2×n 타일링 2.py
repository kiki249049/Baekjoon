import sys

input=sys.stdin.readline
sys.setrecursionlimit(2000)

def factoiral(n) :
    if n <= 1 :
        return 1
    else :
        return n*factoiral(n-1)

N=int(input())
answer=[]
real_answer=0
if N%2 != 0 :
    for i in range(1,N+1,2) :
        a=i
        b=(N-a)//2
        answer.append([a,b])
else :
    for i in range(0,N+1,2) :
        a=i
        b=(N-a)//2
        answer.append([a,b])
for x,y in answer :
    real_answer += (factoiral(x+y)//(factoiral(x)*factoiral(y)))*(2**y)
print(real_answer%10007)