import sys


sys
queue=[]
T=int(sys.stdin.readline())
for i in range(T) :
    a=sys.stdin.readline().rstrip()
    if a.startswith('push') :
        a=list(a.split())
        queue.append(int(a[1]))
    elif a=='front':
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
    elif a=='back':
        if len(queue) == 0:
            print(-1)
        else :
            print(queue[len(queue)-1])
    elif a=='empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif a=='size' :
        print(len(queue))
    else :
        if len(queue) == 0 :
            print(-1)
        else :    
            print(queue.pop(0))                
