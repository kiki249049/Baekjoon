import sys
input = sys.stdin.readline
def table(p) :
    L = len(p)
    tb = [0]*L
    i = 0
    for j in range(1,L) :
        while i > 0 and p[i] != p[j] : # 다르면은 그 전에 그전에 겹친곳까지로 인덱스를 변경
            i = tb[i-1]
        if p[i] == p[j] : # 일치하면 테이블에 일치한 인덱스만큼 갱신을 해줍니다.
            i += 1
            tb[j] = i
    return tb

def KMP(p,t) :
    ans = []
    M = len(p)
    N = len(t)
    table1 = table(p)
    i = 0
    for j in range(N) :
        while i > 0 and p[i] != t[j] :
            i = table1[i-1]
        if p[i] == t[j] :
            if i == M-1 : # 패턴을 찾았다.
                ans.append(j-i+1)
                i=table1[i]
            else :
                i += 1
    return ans
text=input().rstrip()
pattern=input().rstrip()
ans=KMP(pattern,text)
print(len(ans))
print(*ans)