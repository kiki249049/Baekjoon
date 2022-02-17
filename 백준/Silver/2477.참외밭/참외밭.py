K=int(input())
length=[]
minus_area=1
val=0
for i in range(6) :
    d,l = map(int,input().split())
    length.append(l)
max_length = max(length)
idx=[]
for i in range(6) :
    if max_length==length[i] :
        idx.append(i)
if len(idx) == 2 :
    for i in idx :
        minus_area *= abs(length[i-1]-length[(i+1)%6])
    print(K*(max_length**2-minus_area))
else :
    if length[(idx[0]+1)%6] > length[idx[0]-1] :
        val = length[(idx[0]+1)%6]
        idx.append((idx[0]+1)%6)
    else :
        val = length[idx[0]-1]
        idx.append(idx[0]-1)
    for j in idx :
        minus_area *= abs(length[j-1]-length[(j+1)%6])
    print(K*(val*max_length-minus_area))