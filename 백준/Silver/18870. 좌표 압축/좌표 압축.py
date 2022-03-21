import sys
from copy import deepcopy
input = sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))
store=deepcopy(nums)
ans = [0]*N
temp={}
nums=set(nums)
nums=sorted(nums)
for i in range(len(nums)) :
    temp[nums[i]] = i
for i in range(N) :
    if store[i] in temp :
        print(temp[store[i]], end=' ')