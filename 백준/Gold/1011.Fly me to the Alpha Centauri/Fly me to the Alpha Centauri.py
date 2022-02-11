import sys
import math

T=int(sys.stdin.readline())
for i in range(T) :
    x,y = map(int,sys.stdin.readline().split())
    L=y-x
    if math.sqrt(L) == int(math.sqrt(L)) :
        print(2*int(math.sqrt(L))-1)
    else :
        if L < (1+(int(math.sqrt(L))**2)+((int(math.sqrt(L))+1)**2))//2 :
            print(2*int(math.sqrt(L)))
        else :
            print(2*int(math.sqrt(L))+1)