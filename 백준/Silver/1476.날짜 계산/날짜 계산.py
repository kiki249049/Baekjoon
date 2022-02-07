import sys


a,b,c = map(int,sys.stdin.readline().split())
answer=[]
for i in range(20000) :
    if a==15 :
        a=0
    if b==28 :
        b=0
    if c==19 :
        c=0
    if i%15 == a and i%28 == b and i%19==c :
        if i == 0:
            continue
        else :
            answer.append(i)

print(min(answer))