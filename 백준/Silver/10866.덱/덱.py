import sys


sys
T=int(sys.stdin.readline())
Deck=[]
for i in range(T) :
    a=sys.stdin.readline().rstrip()
    if a.startswith("push_back") :
        a=list(a.split())
        Deck.append(int(a[1]))
    elif a.startswith("push_front") :
        a=list(a.split())
        Deck= [a[1]] + Deck
    elif a=='front' :
        if len(Deck) != 0:
            print(Deck[0])
        else :
            print(-1)    
    elif a=='back' :
        if len(Deck) != 0 :
            print(Deck[-1])
        else :
            print(-1)    
    elif a=='pop_front' :
        if len(Deck) != 0 :
            print(Deck.pop(0))
        else :
            print(-1)
    elif a=='pop_back' :
        if len(Deck) != 0 :
            print(Deck.pop(-1))
        else :
            print(-1)
    elif a=='size' :
        print(len(Deck))
    elif a=='empty' :
        if len(Deck) == 0 :
            print(1)
        else :
            print(0)                