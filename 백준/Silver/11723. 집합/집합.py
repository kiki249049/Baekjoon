import sys
input = sys.stdin.readline

def int_chg(char) :
    if char.isdecimal() :
        return int(char)
    else :
        return char

S=set()
M = int(input())
for i in range(M) :
    command=list(map(int_chg,input().split()))
    if len(command) == 1:
        if command[0] == "all" :
            S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        else :
            S = set()
    else :
        if command[0] == "add" :
            S.add(command[1])
        elif command[0] == "remove" :
            S.discard(command[1])
        elif command[0] == "check" :
            if command[1] in S :
                print(1)
            else :
                print(0)
        else :
            if command[1] in S :
                S.discard(command[1])
            else :
                S.add(command[1])