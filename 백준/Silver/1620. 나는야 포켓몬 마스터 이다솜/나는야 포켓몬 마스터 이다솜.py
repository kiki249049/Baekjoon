import sys
input = sys.stdin.readline

N,M=map(int,input().split())
pokemon = {input().rstrip() : i for i in range(1, N + 1)}
reverse_pokemon=dict(map(reversed,pokemon.items()))
for i in range(M) :
    problem=input().rstrip()
    if problem.isdecimal() :
        print(reverse_pokemon[int(problem)])
    else :
        if problem in pokemon :
            print(pokemon[problem])