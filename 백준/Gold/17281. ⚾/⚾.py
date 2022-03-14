import sys
from itertools import permutations
input = sys.stdin.readline
def hit(hit) :
    global out,score,b1,b2,b3
    player = [0]
    if hit == 1 :
        score += b3
        b1,b2,b3 = 1,b1,b2
    elif hit == 2 :
        score += (b2+b3)
        b1,b2,b3 = 0,1,b1
    elif hit == 3 :
        score += (b1+b2+b3)
        b1,b2,b3 = 0,0,1
    else :
        score += (b1+b2+b3+1)
        b1,b2,b3 = 0,0,0

    return


N=int(input())
player_ability = [list(map(int,input().split())) for _ in range(N)]
sequence = list(permutations([2,3,4,5,6,7,8,9],8))
max_score=0
for i in range(len(sequence)) :
    sequence[i]=list(sequence[i][:3]) + [1] + list(sequence[i][3:])
for i in range(len(sequence)) : # 경기수
    today_squad=sequence[i]
    score=0
    h=0
    for k in range(N) : # 이닝 수
        out = 0
        b1,b2,b3 = 0,0,0
        while out < 3 :
            if player_ability[k][today_squad[h]-1] == 0 :
                out += 1
            else :
                hit(player_ability[k][today_squad[h]-1])
            h += 1
            h = h%9
    if score > max_score :
        max_score = score
print(max_score)