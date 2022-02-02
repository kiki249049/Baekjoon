a=[1,1,1]
while a[0] != 0 and a[1] != 0 and a[2] != 0 : 
    a = list(map(int,input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0 :
        break
    c=a.pop(a.index(max(a)))
    answer=0
    for i in a :
        answer += i**2
    if answer == c**2 :
        print('right')
    else : 
        print('wrong')
    a.append(' ')