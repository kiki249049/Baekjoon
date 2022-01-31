T=int(input())
list1=[]
rank=[]
for i in range(T) :
    list1.append(list(map(int,input().split())))
for i in range(T) :
    rank.append(1)    
for i in range(T) :
    for t in range(T) :
        if list1[i][0] < list1[t][0] and list1[i][1] < list1[t][1] :
            rank[i] += 1
        else : 
            continue

print(*rank)
 