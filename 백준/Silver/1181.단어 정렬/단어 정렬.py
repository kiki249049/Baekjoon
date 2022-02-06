import sys


T=int(sys.stdin.readline().rstrip())
array=[]
group_array=[]
answer=[]
for i in range(T) :
    array.append(sys.stdin.readline().rstrip())
L=max(map(lambda x: len(x),array))
for i in range(1,L+1) :
    group_array.append(list(filter(lambda x: len(x)==i,array)))
for i in group_array :
    i=set(i)
    i=list(i)
    i.sort()
    answer.append(i)
for i in answer :
    for k in i :
        print(k)