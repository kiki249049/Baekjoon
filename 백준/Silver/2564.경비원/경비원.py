block=list(map(int,input().split()))
N=int(input())
answer=0
shop=[list(map(int,input().split())) for i in range(N)]
position=list(map(int,input().split()))
if position[0] == 1 :
    for i in shop :
        if i[0] == 1 :
            answer += abs(position[1]-i[1])
        elif i[0] == 3 :
            answer += i[1] + position[1]
        elif i[0] == 4 :
            answer += i[1] + (block[0] - position[1])
        elif i[0] == 2 :
            if position[1] + block[1] + i[1] > block[0]-position[1] + block[1] + block[0]-i[1] :
                answer += block[0]-position[1] + block[1] + block[0]-i[1]
            else :
                answer += position[1] + block[1] + i[1]
elif position[0] == 2 :
    for i in shop :
        if i[0] == 2 :
            answer += abs(position[1]-i[1])
        elif i[0] == 3 :
            answer +=  position[1] + block[1] - i[1]
        elif i[0] == 4 :
            answer += (block[0] - position[1]) + (block[1] - i[1])
        elif i[0] == 1 :
            if position[1] + block[1] + i[1] > block[0]-position[1] + block[1] + block[0]-i[1] :
                answer += block[0]-position[1] + block[1] + block[0]-i[1]
            else :
                answer += position[1] + block[1] + i[1]
elif position[0] == 3 :
    for i in shop :
        if i[0] == 3 :
            answer += abs(position[1]-i[1])
        elif i[0] == 4 :
            if position[1] + block[0] + i[1] > block[1] - position[1] + block[0] + block[1] - i[1]:
                answer += block[1] - position[1] + block[0] + block[1] - i[1]
            else:
                answer += position[1] + block[0] + i[1]
        elif i[0] == 2 :
            answer += i[1] + (block[1] - position[1])
        elif i[0] == 1 :
            answer += i[1] + position[1]
else :
    for i in shop:
        if i[0] == 4:
            answer += abs(position[1] - i[1])
        elif i[0] == 3 :
            if position[1] + block[0] + i[1] > block[1] - position[1] + block[0] + block[1] - i[1]:
                answer += block[1] - position[1] + block[0] + block[1] - i[1]
            else:
                answer += position[1] + block[0] + i[1]
        elif i[0] == 2:
            answer += (block[1] - position[1]) + (block[0] - i[1])
        elif i[0] == 1:
            answer += position[1] +  (block[0] - i[1])
print(answer)

