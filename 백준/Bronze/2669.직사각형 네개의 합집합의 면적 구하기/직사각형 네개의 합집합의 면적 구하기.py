recs=[]
derv=[]
answer=set()
for i in range(4) :
    recs.append(list(map(int,input().split())))
for k in recs :
   for j in range(k[0],k[2]) :
       for p in range(k[1],k[3]) :
           derv=[]
           derv.append(j)
           derv.append(p)
           derv.append(j+1)
           derv.append(p+1)
           derv=tuple(derv)
           answer.add(derv)
print(len(answer))