def factorial(n) :
    if n <= 1 :
        return 1
    else :
        return n*factorial(n-1)

n,m = map(int,input().split())
ans = factorial(n)//(factorial(n-m)*factorial(m))
print(ans)