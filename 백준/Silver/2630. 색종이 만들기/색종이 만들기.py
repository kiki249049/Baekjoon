import sys
input = sys.stdin.readline

def search(paper) :
    global ans0, ans1
    num0 = 0
    num1 = 0
    if len(paper) == 1:
        if paper[0][0] == 1 :
            ans1 += 1
            return
        elif paper[0][0] == 0 :
            ans0 += 1
            return
    else :
        for i in range(len(paper)) :
            for k in range(len(paper)) :
                if paper[i][k] == 1 :
                    num1 += 1
                else :
                    num0 += 1
        if num1 == (len(paper))**2 :
            ans1 += 1
            return
        elif num0 == (len(paper))**2 :
            ans0 += 1
            return
        else :
            search([paper[i][0:len(paper)//2] for i in range(len(paper)//2)])
            search([paper[i][len(paper)//2:len(paper)] for i in range(len(paper)//2)])
            search([paper[i][0:len(paper)//2] for i in range(len(paper)//2,len(paper))])
            search([paper[i][len(paper)//2:len(paper)] for i in range(len(paper)//2,len(paper))])

N=int(input())
ans0 = 0
ans1 = 0
paper = [list(map(int,input().split())) for _ in range(N)]
search(paper)
print(ans0)
print(ans1)