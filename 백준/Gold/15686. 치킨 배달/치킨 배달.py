import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

N,M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)] # 맵을 받고
chicken=[]
ans = 100000
for i in range(N) :  # 치킨집의 좌표를 얻는다.
    for k in range(N) :
        if area[i][k] == 2 :
            chicken.append((i,k))
for C in combinations(chicken,M) : # C는 좌표 조합시킨것.
    temp = [[1000]*N for _ in range(N)] # 최소의 거리를 저장할 temp 가상지형 생성
    val = 0 # 그 가상세계의 합계
    for i in C : # 각 좌표경우에 대해
        for j in range(N) :
            for k in range(N) :
                if area[j][k] == 1: # 집이 발견되면
                    x,y = i
                    distance = abs(x-j)+abs(y-k) # 거리를찾고
                    if temp[j][k] > distance : # 그 거리가 최소치킨거리보다 작으면 갱신
                        temp[j][k] = distance
    for i in range(N) :
        for k in range(N) :
            if temp[i][k] != 1000 :
                val += temp[i][k]
    ans = min(ans,val)
print(ans)