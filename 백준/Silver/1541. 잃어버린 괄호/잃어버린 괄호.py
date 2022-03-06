import sys

input=sys.stdin.readline

math_sentence=input()
number=''
new_sentence=[]
answer=0
operator=["+","-"]
memory=100
for i in range(len(math_sentence)):
    if math_sentence[i] not in operator and (i==len(math_sentence)-1 or math_sentence[i+1] in operator) :
        number += math_sentence[i]
        new_sentence.append(int(number))
        number=''
    elif math_sentence[i] not in operator and (i==len(math_sentence)-1 or math_sentence[i+1] not in operator):
        number += math_sentence[i]
    elif math_sentence[i] in operator :
        new_sentence.append(math_sentence[i])
for i in range(len(new_sentence)) :
    if new_sentence[i] not in operator :
        answer += new_sentence[i]
    elif new_sentence[i] == "+" :
        continue
    elif new_sentence[i]== "-" :
        memory = i
        break
for i in range(memory+1,len(new_sentence)) :
    if new_sentence[i] not in operator:
        answer -= new_sentence[i]
    elif new_sentence[i] == "+":
        continue
    elif new_sentence[i] == "-":
        continue
print(answer)