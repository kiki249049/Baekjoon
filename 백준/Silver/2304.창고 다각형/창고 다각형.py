N=int(input())
list1=[]
answer=0
height=0
for i in range(N) :
    list1.append(list(map(int,input().split())))
list1.sort()
height_box=[]
idx_box=[]
for i in range(len(list1)) :
    height_box.append(list1[i][1])
    idx_box.append(list1[i][0])
height=list1[0][1]
height_idx=list1[0][0]
for i in range(len(list1)):
    if height < list1[i][1] :
        answer += height*(list1[i][0]-height_idx)
        height = list1[i][1]
        height_idx = list1[i][0]
    if list1[i][1] == max(height_box) :
        p=i
        break
answer += height
height_idx = list1[len(list1)-1][0]
height=list1[len(list1)-1][1]
for i in range(len(list1)-1,p-1,-1) :
    if height <= list1[i][1]:
        answer += height * (height_idx - list1[i][0])
        height = list1[i][1]
        height_idx = list1[i][0]
print(answer)