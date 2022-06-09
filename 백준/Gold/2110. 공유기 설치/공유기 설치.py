import sys
input = sys.stdin.readline

def binary_search(start,end) :
    global ans
    while start <= end :
        now = home[0]
        cnt = 1
        gap = (start+end)//2 # 차이
        for i in range(1,len(home)) :
            if home[i] >= now+gap :
                now = home[i]
                cnt += 1
        if cnt >= C :
            start = gap+1
            ans = gap
        else :
            end = gap-1

N,C = map(int,input().split()) # N : 집 , C : 공유기의 갯수
home = []
ans = int(1e9)
for i in range(N) :
    home.append(int(input()))
home.sort()
binary_search(1,home[-1]-home[0])
print(ans)