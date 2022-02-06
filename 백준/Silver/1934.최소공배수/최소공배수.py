import math
import sys


T=int(input())
def minmultiply(a,b) :
    if a==1 or b==1 :
        return a*b
    for i in range(2,a+1):
        if a%i==0 and b%i==0 :
                a=a//i
                b=b//i
                return i*minmultiply(a,b)
        else :
            continue
    return a*b
for i in range(T) :
    A,B = map(int,sys.stdin.readline().split())
    print(minmultiply(A,B))