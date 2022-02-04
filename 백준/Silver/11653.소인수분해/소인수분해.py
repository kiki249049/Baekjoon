
import math
import sys

math
T=int(sys.stdin.readline())
def divide(A) :
    if A == 1 :
        return None
    elif A==2 :
        return print(2)
    for i in range(2,int(math.sqrt(A)+1)+1) :
        if A%i == 0 :
            print(i)
            return divide(A//i)
        else :
            continue
    return print(A)

divide(T)    