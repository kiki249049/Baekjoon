import sys
from collections import deque
input = sys.stdin.readline

def calculator1(a,b,operator) :
    if operator == "+" :
        return a+b
    elif operator == "-" :
        return a-b
    elif operator == "*" :
        return a*b
def calculator2(a,b,c,operator1,operator2) :
    if operator1 == "+" :
        if operator2 == "+" :
            return a+(b+c)
        elif operator2 == "-" :
            return a+(b-c)
        elif operator2 == "*" :
            return a+(b*c)
    if operator1 == "-" :
        if operator2 == "+" :
            return a-(b+c)
        elif operator2 == "-" :
            return a-(b-c)
        elif operator2 == "*" :
            return a-(b*c)
    if operator1 == "*" :
        if operator2 == "+" :
            return a*(b+c)
        elif operator2 == "-" :
            return a*(b-c)
        elif operator2 == "*" :
            return a*(b*c)

def search(lst) :
    queue = deque()
    queue.append(lst) # [val,idx]
    while queue :
        t=queue.popleft()
        if t[1] == len(math_sentence)-1 :
            answers.append(t[0])
        if t[1] == len(math_sentence)-1 :
            answers.append(t[0])
        if t[1]+2 <= len(math_sentence)-1 :
            lst2=[0,0]
            lst2[0] = calculator1(t[0],math_sentence[t[1]+2],math_sentence[t[1]+1])
            lst2[1] = t[1]+2
            queue.append(lst2)
        if t[1]+4 <= len(math_sentence)-1 :
            lst3=[0,0]
            lst3[0] = calculator2(t[0],math_sentence[t[1]+2],math_sentence[t[1]+4],math_sentence[t[1]+1],math_sentence[t[1]+3])
            lst3[1] = t[1]+4
            queue.append(lst3)





N=int(input())
math_sentence=list(input().rstrip())
operator=["+","-","*"]
answers=[]
for i in range(len(math_sentence)) :
    if math_sentence[i] not in operator :
        math_sentence[i] = int(math_sentence[i])
search([math_sentence[0],0])
print(max(answers))