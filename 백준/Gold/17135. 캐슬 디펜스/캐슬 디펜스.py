import sys
import copy
input = sys.stdin.readline

def kill(a,b,c)  :# 한턴에 죽이는 애들
    global ans
    target_a=[]
    target_b=[]
    target_c=[]
    target=set()
    for i in range(N):
        for k in range(M) :
            if abs(a[0]-i)+abs(a[1]-k) <= D and area[i][k] == 1 :
                target_a.append([i,k])
            if abs(b[0]-i)+abs(b[1]-k) <= D and area[i][k] == 1 :
                target_b.append([i,k])
            if abs(c[0]-i)+abs(c[1]-k) <= D and area[i][k] == 1 :
                target_c.append([i,k])
    if target_a :
        target_a.sort(key=lambda x: (abs(x[0]-a[0])+abs(x[1]-a[1]),x[1]))
        target.add(tuple(target_a[0]))
    if target_b :
        target_b.sort(key=lambda x: (abs(x[0]-b[0])+abs(x[1]-b[1]),x[1]))
        target.add(tuple(target_b[0]))
    if target_c :
        target_c.sort(key=lambda x: (abs(x[0]-c[0])+abs(x[1]-c[1]),x[1]))
        target.add(tuple(target_c[0]))
    for i in target :
        p,q = i
        area[p][q] = 0
        ans += 1
    return

N,M,D = map(int,input().split()) # 행의 수 N, 열의 수 M, 궁수의 공격거리 D
area = [list(map(int,input().split())) for _ in range(N)]
re_area = copy.deepcopy(area)
max_ans = 0
for i in range(M) :
    x1,y1 = N,i
    for j in range(y1+1,M) :
        x2,y2 = N,j
        for k in range(y2+1,M) :
            x3, y3 = N,k
            a=[x1,y1]
            b=[x2,y2]
            c=[x3,y3] # 궁수 좌표
            area = copy.deepcopy(re_area)
            ans = 0
            for p in range(N) :
                enemy=[]
                temp = [[0] * M for _ in range(N)]
                kill(a,b,c)  # 궁수가 죽임
                for s in range(N):  # 한칸씩움직
                    for f in range(M):
                        if area[s][f] == 1:
                            area[s][f] = 0
                            if s + 1 < N:
                                enemy.append([s, f])
                for e, q in enemy:
                    temp[e + 1][q] = 1
                area = temp
            if ans > max_ans :
                max_ans = ans
print(max_ans)