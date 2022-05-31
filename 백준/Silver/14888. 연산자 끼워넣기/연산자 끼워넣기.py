import sys
from itertools import permutations
input = sys.stdin.readline

def oper(num1,num2,op) :
    if op == 0 : # 덧셈
        return num1 + num2
    elif op == 1 : # 뺄셈
        return num1 - num2
    elif op == 2 : # 곱셈
        return num1*num2
    else : # 나눗셈
        if num1 < 0 :
            return -(-num1//num2)
        else :
            return num1//num2

N = int(input())
numbers = list(map(int,input().split()))
operator = list(map(int,input().split()))
operator_lst = []
max_val = -int(1e9)
min_val = int(1e9)
for idx,value in enumerate(operator) :
    for i in range(value) :
        operator_lst.append(idx)
go = set(permutations(operator_lst))
for seq in go :
    val = numbers[0]
    for i in range(len(seq)):
        val=oper(val,numbers[i+1],seq[i])
    if val > max_val :
        max_val = val
    if val < min_val :
        min_val = val
print(max_val,min_val,sep='\n')