import sys

input = sys.stdin.readline

N=int(input())
dp=1
conference=[]
for i in range(N) :
    conference.append(list(map(int,input().split())))
conference.sort()
end=conference[0][1]
for i in range(1,N) :
    if conference[i][0] >= end :
        end = conference[i][1]
        dp += 1
    elif conference[i][1] <= end :
        end = conference[i][1]
print(dp)