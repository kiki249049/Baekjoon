burgers=[]
beverages=[]
for i in range(3) :
    burgers.append(input())
for i in range(2) :
    beverages.append(input())
burgers=map(int,burgers)
beverages=map(int,beverages)
print(min(burgers)+min(beverages)-50)
