A=int(input())
real_answer=[]
def solution(a,p) :
    if a-p < 0 :
        return None
    else :
        answer.append(a-p)
        return solution(p,a-p)
for i in range(1,A+1) :
    answer=[]
    answer.append(A)
    answer.append(i)
    solution(A,i)
    if len(answer) > len(real_answer) :
        real_answer=answer
print(len(real_answer))
print(*real_answer)