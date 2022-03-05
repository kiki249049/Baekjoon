import sys

input=sys.stdin.readline

N,K = map(int,input().split())
coin=[]
answer=0
for i in range(N) :
    coin.append(int(input()))
for i in range(len(coin)-1,-1,-1) :
    answer += K//coin[i]
    K = K%coin[i]
print(answer)