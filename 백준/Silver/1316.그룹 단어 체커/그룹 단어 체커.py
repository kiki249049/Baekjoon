import sys


T=int(sys.stdin.readline())
words=[]
box=[]
answer=0
for i in range(T) :
    words.append(sys.stdin.readline().rstrip())
for i in words :
    if len(i) == 1 :
        answer += 1
        continue
    i += "0"
    for k in range(len(i)-1) :
        if i[k] != i[k+1] :
            box.append(i[k])
        else :
            continue
    for j in box :
        if box.count(j) > 1 :
            answer -= 1
            break
        else :
            continue
    box=[]
    answer += 1

print(answer)        
           