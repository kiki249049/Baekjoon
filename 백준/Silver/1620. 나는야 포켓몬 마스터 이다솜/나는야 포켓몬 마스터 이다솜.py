import sys
input = sys.stdin.readline


pokemon={}
N,M=map(int,input().split())
for i in range(1,N+1) :
    pokemon[i] = input().rstrip()
reverse_pokemon=dict(map(reversed,pokemon.items()))
for i in range(M) :
    problem=input().rstrip()
    if problem.isdecimal() :
        print(pokemon[int(problem)])
    else :
        if problem in reverse_pokemon :
            print(reverse_pokemon[problem])