import sys


N,K=map(int,sys.stdin.readline().split())
temperatures=list(map(int,sys.stdin.readline().split()))
answers=[]
val1=0
max_val=0
for i in range(K) :
    val1 += temperatures[i]
max_val=val1
for i in range(N-K) : 
    val1=val1-temperatures[i]+temperatures[i+K]
    if val1 > max_val :
        max_val=val1
print(max_val)