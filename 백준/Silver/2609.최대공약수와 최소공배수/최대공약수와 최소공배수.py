a,b=map(int,input().split())
box=[]
minimum=1
maximum=0
def solution(a,b) :
    if a==1 or b==1 :
        return 1
    for i in range(2,10000):
        if a%i == 0 and b%i == 0 :
            box.append(i)
            a=a//i
            b=b//i
            return solution(a,b)
        else :
            continue
    return 1
solution(a,b)    
for i in box :
    minimum *= i
maximum=(a*b)//minimum
print(f'{minimum}\n{maximum}')    
