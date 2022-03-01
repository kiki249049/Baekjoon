import sys
input=sys.stdin.readline

def binarysearch(A,n) :
    start=0
    end=len(A)-1
    while start <= end :
        middle = (start + end) // 2
        if A[middle] == n :
            print(1)
            return
        elif A[middle] > n :
            end = middle - 1
        else :
            start = middle + 1
    print(0)
    return


N=int(input())
A=list(map(int,input().split()))
M=int(input())
search=list(map(int,input().split()))
A.sort()
for i in search:
    binarysearch(A,i)