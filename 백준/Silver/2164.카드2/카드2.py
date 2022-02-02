from collections import deque
import sys

sys
deque
N=int(sys.stdin.readline())
card=[]
card=deque(card)
box=[]
for i in range(1,N+1) :
    card.append(i)
while len(card) != 1 :
        card.popleft() 
        card.rotate(-1) 
print(card[0])