def operator_push(operator):
    global token, numbers
    if len(token) == 0 :
        token.append(operator)
        return
    for i in range(len(operators)) :
        if operator == operators[i] :
            for k in range(len(operators)):
                if token[-1] == operators[k] :
                    if icp[i] > isp[k] :
                        token.append(operator)
                        return
                    else :
                        numbers.append(token.pop())
                        operator_push(operator)
                        return


calculate=list(input())
calculate.append(")")
calculate = ["("] + calculate
operators=[")","*","/","+","-","("]
isp=["-",2,2,1,1,0]
icp=["-",2,2,1,1,3]
token=[]
numbers=[]
for i in calculate :
    if i in operators :
        if i == ")" :
            while True :
                a=token.pop()
                if a=="(" :
                    break
                numbers.append(a)
        else :
            operator_push(i)
    else :
        numbers.append(i)
print(''.join(map(str,numbers)))