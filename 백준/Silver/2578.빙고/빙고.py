def bingo_check(a) :
    val1=0
    val2=0
    val3=0
    val4=0
    sum=0
    for i in range(5) :
        val1=0
        val4=0
        for k in range(5):
            val1 += a[i][k]
            val4 += a[k][i]
        if val1 == 0 :
            sum += 1
        if val4 == 0 :
            sum += 1
    for i in range(5) :
        val2 += a[i][i]
        val3 += a[i][4-i]
    if val2 == 0 :
        sum += 1
    if val3 == 0 :
        sum += 1
    if sum >= 3 :
        return 1
    return 0
def bingo_number(a,n) :
    global count
    for i in range(5):
        for k in range(5):
            if a[i][k] == n :
                a[i][k] = 0
    count += 1
    return a


count = 0
bingo=[list(map(int,input().split())) for i in range(5)]
check_number=[list(map(int,input().split())) for k in range(5)]
for i in range(5):
    for k in range(5):
        answer=0
        answer=bingo_check(bingo_number(bingo,check_number[i][k]))
        if answer == 1 :
            print(count)
            break
    if answer == 1:
        break
