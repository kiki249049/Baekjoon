import math
import sys

math
sys
M,N = map(int,input().split())
answer_key=0
if M==1:
    M=2
for i in range(M,N+1) :
    answer_key=0
    for k in range(2,int(math.sqrt(i)+1)):
        if i%k == 0 and i != k :
            answer_key=1
            break
    if answer_key==0:
        print(i, end='\n')