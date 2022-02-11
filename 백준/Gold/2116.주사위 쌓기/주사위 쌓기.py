import sys

T=int(input())
Dices=[]
for i in range(T) :
    Dice=list(map(int,sys.stdin.readline().split()))
    Dices.append(Dice)
answer_list=[]
def Pair(Dice,idx) :
    global answer
    if idx == 0 :
        a=Dice[0]
        b=Dice[5]
        Dice[0] = 0
        Dice[5] = 0
        answer += max(Dice)
        Dice[0]=a
        Dice[5]=b
        return Dice[5]
    elif idx == 1 :
        a = Dice[1]
        b = Dice[3]
        Dice[1] = 0
        Dice[3] = 0
        answer += max(Dice)
        Dice[1] = a
        Dice[3] = b
        return Dice[3]
    elif idx == 2 :
        a = Dice[2]
        b = Dice[4]
        Dice[2] = 0
        Dice[4] = 0
        answer += max(Dice)
        Dice[2] = a
        Dice[4] = b
        return Dice[4]
    elif idx == 3 :
        a = Dice[3]
        b = Dice[1]
        Dice[3] = 0
        Dice[1] = 0
        answer += max(Dice)
        Dice[3] = a
        Dice[1] = b
        return Dice[1]
    elif idx == 4 :
        a = Dice[4]
        b = Dice[2]
        Dice[4] = 0
        Dice[2] = 0
        answer += max(Dice)
        Dice[4] = a
        Dice[2] = b
        return Dice[2]
    else :
        a = Dice[5]
        b = Dice[0]
        Dice[5] = 0
        Dice[0] = 0
        answer += max(Dice)
        Dice[5] = a
        Dice[0] = b
        return Dice[0]
for idx2 in range(6) :
    answer = 0
    for k in range(len(Dices)-1) :
        idx2=Dices[k+1].index(Pair(Dices[k],idx2))
    Pair(Dices[len(Dices)-1],idx2)
    answer_list.append(answer)
print(max(answer_list))
