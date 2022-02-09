T=int(input())
switch=list(map(int,input().split()))
N=int(input())
def boy(B) :
    for i in range(1,len(switch)+1) :
        if i%B == 0 :
            if switch[i-1] == 1 :
                switch[i-1] = 0
            else :
                switch[i-1] = 1
        else :
            continue
    return switch

def girl(B) :
    i=0
    if switch[B-1] == 0 :
        switch[B-1] = 1
    else : 
        switch[B-1] = 0
    while (B-2-i) >=0 and (B+i) <= (len(switch)-1) and switch[B-2-i] == switch[B+i] :
        if switch[B-2-i] == 1 :
            switch[B-2-i] = 0
            switch[B+i] = 0
        else :
            switch[B-2-i] = 1
            switch[B+i] = 1
        i += 1
    return switch    

for i in range(N) :
    A,B=map(int,input().split())
    if A == 1 :
        boy(B)
    else :
        girl(B)
while len(switch) >= 20 :
    answer=[]
    for i in range(20):
        answer.append(switch.pop(0))
    print(*answer)
print(*switch)