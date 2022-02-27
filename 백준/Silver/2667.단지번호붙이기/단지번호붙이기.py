import sys
from collections import deque
def bfs(x,y) :
    cnt=1
    city[x][y] = 2
    queue=deque()
    queue.append([x,y])
    while queue :
        p,q=queue.popleft()
        for dp,dq in [[-1,0],[0,-1],[1,0],[0,1]] :
            np,nq = p+dp , q+dq
            if 0<=np<N and 0<=nq<N and city[np][nq] == 1 :
                queue.append([np,nq])
                city[np][nq] = 2
                cnt += 1
    return cnt


N=int(sys.stdin.readline())
city=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
city_num=0
house_cnt=[]
for i in range(N):
    for k in range(N) :
        if city[i][k] == 1 :
            house_cnt.append(bfs(i,k))
            city_num += 1
print(city_num)
house_cnt.sort()
for i in house_cnt :
    print(i)