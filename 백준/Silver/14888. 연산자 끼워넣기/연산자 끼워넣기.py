import sys
input = sys.stdin.readline


def dfs(idx,val,pl,mi,mu,div) :
    global max_val,min_val
    if idx == N :
        if val > max_val :
            max_val = val
        if val < min_val :
            min_val = val
    else :
        if pl > 0 :
            dfs(idx+1,val+num[idx],pl-1,mi,mu,div)
        if mi > 0 :
            dfs(idx + 1, val - num[idx], pl, mi-1, mu, div)
        if mu > 0 :
            dfs(idx + 1, val * num[idx], pl , mi, mu-1, div)
        if div > 0 :
            if val > 0 :
                dfs(idx + 1, val // num[idx], pl , mi, mu, div-1)
            else :
                dfs(idx + 1, -(-val // num[idx]), pl , mi, mu, div-1)

N = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))
val = 0
max_val = -int(1e9)
min_val = int(1e9)
dfs(1,num[0],op[0],op[1],op[2],op[3])
print(max_val,min_val,sep='\n')
