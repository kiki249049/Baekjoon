N,K = map(int,input().split())
list1=[]
list2=[]
div = 0
answer=[]
for i in range(1,N+1) :
    list1.append(i)
for i in range(N) :
    div = K%len(list1)
    answer.append(list1.pop(div-1))
    list2=[0]*len(list1)
    if div == 0 :
        for j in range(len(list1)):
            list2[j]=list1[j]
    else :
        for j in range(len(list1)):
            list2[j-(div-1)]=list1[j]
    list1=list2
answer=str(list(map(int,answer)))
answer=answer.replace('[','<',1)
answer=answer.replace(']','>',1)    
print(answer)  