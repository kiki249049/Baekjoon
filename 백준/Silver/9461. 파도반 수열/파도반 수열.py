import sys
input = sys.stdin.readline

def surf(n) :
    if not P[n] :
        P[n] = surf(n-1) + surf(n-5)
        return P[n]
    else:
        return P[n]


T=int(input())
for i in range(T):
    n=int(input())
    P=[0,1,1,1,2,2]
    for i in range(95):
        P.append(0)
    print(surf(n))