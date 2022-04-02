import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    dp0 = [0]*N
    dp1 = [0]*N
    sticker = [list(map(int,input().split())) for _ in range(2)]
    if N >= 2 :
        dp0[0] = sticker[0][0]
        dp1[0] = sticker[1][0]
        dp0[1] = dp1[0]+sticker[0][1]
        dp1[1] = dp0[0]+sticker[1][1]
    else :
        dp0[0] = sticker[0][0]
        dp1[0] = sticker[1][0]
    i = 0
    k = 2
    if N >= 3 :
        while k < N : # k는 진행상태 i는 스티커 선택하는 위치
            dp0[k] = max(dp1[k-1]+sticker[0][k],dp1[k-2]+sticker[0][k])
            dp1[k] = max(dp0[k-1]+sticker[1][k],dp0[k-2]+sticker[1][k])
            k += 1
            i += 1
        print(max(dp0[N-1],dp1[N-1]))
    else :
        print(max(dp0[N-1],dp1[N-1]))