import sys
input = sys.stdin.readline

def pre_order(n) :
    if n :
        print(chr(n+64),end='')
        pre_order(ch1[n])
        pre_order(ch2[n])
def in_order(n) :
    if n :
        in_order(ch1[n])
        print(chr(n+64),end='')
        in_order(ch2[n])
def post_order(n) :
    if n :
        post_order(ch1[n])
        post_order(ch2[n])
        print(chr(n+64),end='')

N = int(input())
ch1=[0]*27
ch2=[0]*27
for i in range(N) :
    p,c1,c2 = map(ord,input().split())
    p,c1,c2 = p-64,c1-64,c2-64
    if c1 > 0:
        ch1[p] = c1
    if c2 > 0 :
        ch2[p] = c2
pre_order(1)
print()
in_order(1)
print()
post_order(1)