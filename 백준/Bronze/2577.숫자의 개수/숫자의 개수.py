a=int(input())
b=int(input())
c=int(input())
answer = 0
val=a*b*c
list_val = list(str(val))
for i in range(10) :
    answer = 0
    for k in list(map(int,list_val)) :
        if k == i :
            answer += 1 
    print(answer)      