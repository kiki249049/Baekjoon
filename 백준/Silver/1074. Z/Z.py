import sys
imput = sys.stdin.readline

N,r,c = map(int,input().split())
ans=0
r += 1
c += 1
while True :
    if 0 < r <= 2**(N-1) and 0 < c <= 2**(N-1): # 1번 영역 (1,1)
        N -= 1
    elif 0 < r <= 2**(N-1) and 2**(N-1) < c <= 2**(N): # 2번 영역 (1,2)
        ans += 2**(2*(N-1))
        c -= 2**(N-1)
        N -= 1
    elif 2**(N-1) < r <= 2**(N) and 0 < c <= 2**(N-1): # 3번 영역 (2,1)
        ans += 2**(2*(N-1))*2
        r -= 2**(N-1)
        N -= 1
    elif 2**(N-1) < r <= 2**(N) and 2**(N-1) < c <= 2**(N): # 4번 영역 (2,2)
        ans += 2**(2*(N-1))*3
        c -= 2**(N-1)
        r -= 2**(N-1)
        N -= 1
    if N == 0 :
        break
print(ans)