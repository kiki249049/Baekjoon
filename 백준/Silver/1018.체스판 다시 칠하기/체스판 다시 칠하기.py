N,M=map(int,input().split())
list1=[]
modify=0
modify_zone=[]
reverse_modify_zone=[]
answer=[]
sample1=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
for i in range(N) :
    list1.append(input())
for p in range(N-7) :
    for i in range(M-7):
        modify_zone.append(modify)
        modify=0
        for j in range(p,p+8) :
            for k in range(i,i+8) :
                if list1[j][k] != sample1[j-p][k-i] :
                    modify += 1
modify_zone.append(modify)
modify_zone.pop(0)
for i in modify_zone :
    reverse_modify_zone.append(64-i)
answer=modify_zone+reverse_modify_zone
print(min(answer))