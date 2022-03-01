import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
M=int(input())
search=list(map(int,input().split()))
numbers=[0] * 20000001
for i in A :
    numbers[i+10000000] += 1
for i in search :
    print(numbers[i+10000000],end=' ')